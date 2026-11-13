"""Web UI + webhook for the RCSA Evidence & Challenge Agent. Standard library only (no Flask needed).

Start:   python web_app.py            then open http://localhost:8000
Webhook: POST http://localhost:8000/api/run   {"process": "Payment Processing"}   (this is what n8n calls)

Optional .env settings:
  WEBHOOK_TOKEN=some-secret     -> webhook callers must send header  X-Token: some-secret
  PORT=8000
"""
import csv
import io
import json
import os
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from rcsa_agent.data_loader import _read_text, find_default_csv
from rcsa_agent.envloader import load_env

load_env()
RUN_LOCK = threading.Lock()  # one agent run at a time (keeps API calls and demo simple)


def sheet_path() -> str:
    return os.environ.get("RCSA_SHEET_URL", "").strip() or find_default_csv() or ""


def list_processes() -> list:
    path = sheet_path()
    if not path:
        return []
    rows = csv.DictReader(io.StringIO(_read_text(path)))
    names = {(r.get("Process") or "").strip() for r in rows}
    return sorted(n for n in names if n)


def run_agent(process: str, use_llm: bool, use_external: bool) -> dict:
    from rcsa_agent.graph import build_graph  # imported here so the page loads even if langgraph is missing
    final = build_graph().invoke({
        "data_path": "", "process": process, "out_dir": "outputs/reports",
        "use_llm": use_llm, "use_external": use_external, "run_log": [],
    })
    report_md = ""
    if final.get("report_path") and Path(final["report_path"]).exists():
        report_md = Path(final["report_path"]).read_text(encoding="utf-8")
    return {
        "status": final.get("status"), "process": process,
        "report_path": final.get("report_path"), "log_path": final.get("log_path"),
        "error": final.get("fatal_error", ""), "run_log": final.get("run_log", []),
        "report_markdown": report_md,
    }


JOBS = {}
NODE_ORDER = ["validate_input", "apply_rules", "retrieve_evidence", "external_research",
              "llm_challenge", "build_report", "finalize"]


def _node_status(name: str, log: list) -> str:
    sts = [e.get("status") for e in log if e.get("node") == name]
    if "failed" in sts:
        return "failed"
    if any(x in ("warning", "degraded") for x in sts):
        return "warn"
    if sts and all(x == "skipped" for x in sts):
        return "skipped"
    return "ok"


def _job_worker(job_id: str, process: str, use_llm: bool, use_external: bool) -> None:
    job = JOBS[job_id]
    try:
        from rcsa_agent.graph import build_graph
        init = {"data_path": "", "process": process, "out_dir": "outputs/reports",
                "use_llm": use_llm, "use_external": use_external, "run_log": []}
        final = {}
        for update in build_graph().stream(init, stream_mode="updates"):
            for node, out in update.items():
                out = out or {}
                job["log"].extend(out.get("run_log", []))
                job["details"][node] = " | ".join(e.get("detail", "") for e in out.get("run_log", []))[:600]
                job["done"].append(node)
                for k in ("status", "report_path", "log_path", "fatal_error"):
                    if k in out:
                        final[k] = out[k]
        report_md = ""
        if final.get("report_path") and Path(final["report_path"]).exists():
            report_md = Path(final["report_path"]).read_text(encoding="utf-8")
        job["result"] = {"status": final.get("status"), "report_path": final.get("report_path"),
                         "error": final.get("fatal_error", ""), "report_markdown": report_md}
    except Exception as exc:
        job["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        job["finished"] = True
        RUN_LOCK.release()


LATEST = {"id": None}


def start_job(process: str, use_llm: bool, use_external: bool) -> str:
    """Create a job and run it in the background. The caller must already hold RUN_LOCK."""
    job_id = uuid.uuid4().hex[:8]
    JOBS[job_id] = {"done": [], "log": [], "details": {}, "finished": False, "process": process,
                    "error": "", "result": None, "t0": time.time()}
    LATEST["id"] = job_id
    threading.Thread(target=_job_worker, args=(job_id, process, use_llm, use_external), daemon=True).start()
    return job_id


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, ctype: str = "application/json") -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, obj) -> None:
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, PAGE.encode("utf-8"), "text/html")
        elif self.path == "/api/processes":
            try:
                self._json(200, {"processes": list_processes(), "source": sheet_path()})
            except Exception as exc:
                self._json(500, {"error": f"{type(exc).__name__}: {exc}"})
        elif self.path.startswith("/api/job/"):
            job = JOBS.get(self.path.rsplit("/", 1)[-1])
            if not job:
                return self._json(404, {"error": "unknown job"})
            nodes = []
            active_set = False
            for name in NODE_ORDER:
                if name in job["done"]:
                    st = _node_status(name, job["log"])
                elif job["finished"]:
                    st = "skipped"
                elif not active_set:
                    st, active_set = "active", True
                else:
                    st = "pending"
                nodes.append({"name": name, "status": st, "detail": job["details"].get(name, "")})
            self._json(200, {"nodes": nodes, "finished": job["finished"], "error": job["error"],
                             "result": job["result"], "elapsed": round(time.time() - job["t0"], 1)})
        elif self.path == "/api/latest":
            jid = LATEST["id"]
            self._json(200, {"job": jid, "finished": (JOBS[jid]["finished"] if jid else True)})
        elif self.path == "/api/health":
            self._json(200, {"ok": True})
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path not in ("/api/run", "/api/start"):
            return self._json(404, {"error": "not found"})
        token = os.environ.get("WEBHOOK_TOKEN", "").strip()
        if token and self.headers.get("X-Token", "") != token:
            return self._json(401, {"error": "bad or missing X-Token header"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length) or b"{}")
        except Exception:
            return self._json(400, {"error": "body must be JSON"})
        process = str(data.get("process") or "Payment Processing").strip()
        use_llm = bool(data.get("use_llm", True))
        use_external = bool(data.get("use_external", False))
        if not RUN_LOCK.acquire(blocking=False):
            return self._json(409, {"error": "another run is in progress, try again in a minute"})
        job_id = start_job(process, use_llm, use_external)
        if self.path == "/api/start":  # started from the web page button
            return self._json(200, {"job": job_id})
        # /api/run: used by n8n. Wait for the run, so n8n gets the final result.
        # The web page follows the same job live, so the planets move when n8n triggers a run.
        job = JOBS[job_id]
        while not job["finished"]:
            time.sleep(0.3)
        if job["error"]:
            return self._json(500, {"error": job["error"]})
        res = job["result"] or {}
        self._json(200, {"status": res.get("status"), "process": process, "report_path": res.get("report_path"),
                         "log_path": None, "error": res.get("error", ""), "run_log": job["log"],
                         "report_markdown": res.get("report_markdown", "")})

    def log_message(self, fmt, *args):
        print("[web]", fmt % args)


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>RCSA Evidence &amp; Challenge Agent</title>
<style>
:root{--bg:#f6f7f9;--card:#fff;--ink:#1c2430;--mut:#667085;--line:#e2e5ea;--acc:#1f4ed8;--ok:#127a3e;--warn:#a15c00;--bad:#b42318}
@media(prefers-color-scheme:dark){:root{--bg:#12161c;--card:#1a2029;--ink:#e8ecf2;--mut:#98a2b3;--line:#2b3340;--acc:#6b93ff;--ok:#4cc38a;--warn:#f0b04a;--bad:#ff7b72}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:20px 16px 60px}
h1{font-size:22px;margin:0 0 2px}.sub{color:var(--mut);margin:0 0 18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;margin-bottom:16px}
.row{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
select,button{font:inherit;padding:9px 12px;border-radius:8px;border:1px solid var(--line);background:var(--card);color:var(--ink)}
button.go{background:var(--acc);color:#fff;border-color:var(--acc);font-weight:600;cursor:pointer}
button.go:disabled{opacity:.5;cursor:wait}
label{display:flex;gap:6px;align-items:center;color:var(--mut)}
.pill{display:inline-block;padding:2px 10px;border-radius:99px;font-weight:600;font-size:13px;border:1px solid var(--line)}
.ok{color:var(--ok)}.warn{color:var(--warn)}.bad{color:var(--bad)}
.steps{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.step{padding:4px 10px;border:1px solid var(--line);border-radius:6px;font-size:13px;color:var(--mut)}
.step.ok{color:var(--ok)}.step.warn{color:var(--warn)}.step.bad{color:var(--bad)}
table{border-collapse:collapse;width:100%;margin:10px 0;font-size:14px;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{background:var(--bg)}
#report h1{font-size:20px}#report h2{font-size:17px;margin-top:22px}#report h3{font-size:15px}
.mut{color:var(--mut)}
.flow{display:flex;align-items:stretch;gap:0;flex-wrap:wrap;row-gap:14px;margin-top:6px}
.node{width:118px;border:2px solid var(--line);border-radius:10px;padding:8px 6px;text-align:center;background:var(--card);transition:all .3s}
.node .t{font-weight:600;font-size:12.5px}.node .s{font-size:11px;color:var(--mut);margin-top:3px;min-height:14px}
.node .d{font-size:11.5px;color:var(--ink);margin-top:5px}
.node.active{border-color:var(--acc);animation:pulse 1s infinite;box-shadow:0 0 0 0 var(--acc)}
.node.ok{border-color:var(--ok)}.node.ok .s{color:var(--ok)}
.node.warn{border-color:var(--warn)}.node.warn .s{color:var(--warn)}
.node.failed{border-color:var(--bad)}.node.failed .s{color:var(--bad)}
.node.skipped{opacity:.45;border-style:dashed}
.link{width:26px;align-self:center;height:3px;background:var(--line);position:relative;overflow:hidden;border-radius:2px}
.link.on{background:var(--ok)}
.link.flow-on{background:repeating-linear-gradient(90deg,var(--acc) 0 6px,transparent 6px 12px);background-size:24px 3px;animation:slide .5s linear infinite}
.node{cursor:pointer}.node.sel{outline:2px solid var(--acc);outline-offset:2px}
.info{margin-top:16px;border-top:1px solid var(--line);padding-top:12px}
.info h3{margin:0 0 6px;font-size:15px}.info ul{margin:6px 0 8px 18px;padding:0}.info li{margin:3px 0}
.info .live{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:13px;margin-top:6px}
@keyframes slide{to{background-position:24px 0}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(107,147,255,.55)}70%{box-shadow:0 0 0 10px rgba(107,147,255,0)}100%{box-shadow:0 0 0 0 rgba(107,147,255,0)}}

.space{position:relative;overflow:hidden;--s:clamp(46px,6vw,72px);--card:#070b1a;--bg:#0b1030;--ink:#e8ecff;--mut:#9aa6d6;--line:#26305c;--acc:#7aa2ff;--ok:#4ade80;--warn:#fbbf24;--bad:#ff6b6b;color:var(--ink);border-color:#26305c;
 background:radial-gradient(ellipse at 15% 0%,#241a6b 0,transparent 55%),radial-gradient(ellipse at 95% 100%,#10336e 0,transparent 55%),#04060f}
.space canvas{position:absolute;inset:0;width:100%;height:100%;z-index:0}
.z{position:relative;z-index:1}
.stage{position:relative;height:250px;margin-top:6px}
#orbits{position:absolute;left:0;top:0;width:100%;height:100%;z-index:0;pointer-events:none}
#orbits .seg{stroke:#3a4a8c;stroke-width:2;stroke-dasharray:3 7;fill:none}
#orbits .seg.done{stroke:var(--ok);stroke-dasharray:none;opacity:.7}
#orbits .seg.go{stroke:#ffd27a;stroke-width:3;stroke-dasharray:8 8;animation:dash .6s linear infinite}
@keyframes dash{to{stroke-dashoffset:-16}}
.planets{position:relative;z-index:1;display:flex;justify-content:space-between;align-items:center;height:100%}
.pl{width:14.28%;display:flex;flex-direction:column;align-items:center;cursor:pointer;text-align:center}
.pl:nth-child(odd){transform:translateY(-34px)}.pl:nth-child(even){transform:translateY(30px)}
.ow{position:relative;width:var(--s);height:var(--s)}
.orb{width:100%;height:100%;border-radius:50%;background:radial-gradient(circle at 30% 28%,var(--c1),var(--c2) 62%,#02030a 130%);box-shadow:inset -9px -9px 20px rgba(0,0,0,.6);transition:transform .4s,filter .4s,box-shadow .4s}
.ow.ring::before{content:"";position:absolute;left:-26%;right:-26%;top:40%;height:20%;border:3px solid rgba(255,225,170,.65);border-radius:50%;transform:rotate(-18deg);z-index:2;pointer-events:none}
.moon{display:none}
.pl.active .moon{display:block;position:absolute;inset:-16px;animation:spin 1.6s linear infinite}
.moon::after{content:"";position:absolute;top:0;left:50%;width:9px;height:9px;margin-left:-4px;border-radius:50%;background:#fff;box-shadow:0 0 10px #fff}
@keyframes spin{to{transform:rotate(360deg)}}
.bd{position:absolute;right:-6px;top:-6px;min-width:20px;height:20px;border-radius:50%;background:#0b1030;border:2px solid var(--line);font-size:12px;font-weight:700;line-height:16px;display:none}
.pl.ok .bd,.pl.warn .bd,.pl.failed .bd,.pl.skipped .bd{display:block}
.pl.ok .bd{border-color:var(--ok);color:var(--ok)}.pl.warn .bd{border-color:var(--warn);color:var(--warn)}.pl.failed .bd{border-color:var(--bad);color:var(--bad)}
.pl.pending .orb{filter:grayscale(.85) brightness(.4)}
.pl.skipped .orb{filter:grayscale(1) brightness(.45);opacity:.6}
.pl.active .orb{transform:scale(1.18);animation:glow 1.2s ease-in-out infinite}
@keyframes glow{0%,100%{box-shadow:inset -9px -9px 20px rgba(0,0,0,.6),0 0 14px var(--c1)}50%{box-shadow:inset -9px -9px 20px rgba(0,0,0,.6),0 0 38px var(--c1)}}
.pl.ok .orb{box-shadow:inset -9px -9px 20px rgba(0,0,0,.6),0 0 16px rgba(74,222,128,.75)}
.pl.warn .orb{box-shadow:inset -9px -9px 20px rgba(0,0,0,.6),0 0 16px rgba(251,191,36,.85)}
.pl.failed .orb{box-shadow:inset -9px -9px 20px rgba(0,0,0,.6),0 0 16px rgba(255,107,107,.9)}
.pl.sel .pn{text-decoration:underline}
.pn{font-size:12.5px;font-weight:600;margin-top:10px}.ps{font-size:11px;color:var(--mut)}
.sub{font-size:11px;color:var(--ink);opacity:.85;margin-top:3px;line-height:1.25}
#ship{position:absolute;z-index:3;font-size:30px;left:0;top:0;pointer-events:none;
 transform:translate(-50%,-50%) rotate(var(--rot,0deg));filter:drop-shadow(0 0 10px #ffb347);
 transition:left 1s cubic-bezier(.55,0,.25,1),top 1s cubic-bezier(.55,0,.25,1)}
</style></head><body><div class="wrap">
<h1>RCSA Evidence &amp; Challenge Agent</h1>
<p class="sub">Second Line operational risk. Synthetic data. Flags and challenges only; a human reviewer decides.</p>

<div class="card">
  <div class="row">
    <select id="proc"><option>Loading processes…</option></select>
    <label><input type="checkbox" id="llm" checked> LLM challenge (OpenAI)</label>
    <label><input type="checkbox" id="ext"> External research (Wikipedia / Tavily)</label>
    <button class="go" id="run">Run agent</button>
  </div>
  <div class="mut" id="src" style="margin-top:8px"></div>
</div>

<div class="card space" id="flowcard" style="display:none">
  <canvas id="stars"></canvas>
  <div class="row z"><strong>Agent mission</strong> <span class="mut" id="timer"></span></div>
  <div class="stage z" id="stage">
    <svg id="orbits"></svg>
    <div class="planets" id="flow"></div>
    <div id="ship">&#128640;</div>
  </div>
  <div class="info z" id="info"></div>
</div>
<div class="card" id="result" style="display:none">
  <div class="row"><strong>Run status:</strong> <span class="pill" id="status"></span> <span class="mut" id="path"></span></div>
</div>
<div class="card" id="reportcard" style="display:none"><div id="report"></div></div>
</div>
<script>
const $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const inline=s=>esc(s).replace(/\*\*(.+?)\*\*/g,"<strong>$1</strong>").replace(/`(.+?)`/g,"<code>$1</code>");
function md(src){
  const L=src.split("\n"),o=[];let i=0,inList=false;
  const closeList=()=>{if(inList){o.push("</ul>");inList=false}};
  while(i<L.length){
    const l=L[i];
    if(/^\s*\|/.test(l)&&i+1<L.length&&/^\s*\|[\s:|-]+\|\s*$/.test(L[i+1])){
      closeList();const cells=r=>r.trim().replace(/^\||\|$/g,"").split("|").map(c=>c.trim());
      let t="<table><tr>"+cells(l).map(c=>"<th>"+inline(c)+"</th>").join("")+"</tr>";i+=2;
      while(i<L.length&&/^\s*\|/.test(L[i])){t+="<tr>"+cells(L[i]).map(c=>"<td>"+inline(c)+"</td>").join("")+"</tr>";i++}
      o.push(t+"</table>");continue}
    let m;
    if(m=l.match(/^(#{1,4})\s+(.*)/)){closeList();o.push(`<h${m[1].length}>${inline(m[2])}</h${m[1].length}>`)}
    else if(m=l.match(/^\s*[-*]\s+(.*)/)){if(!inList){o.push("<ul>");inList=true}o.push("<li>"+inline(m[1])+"</li>")}
    else if(l.trim()===""){closeList()}
    else{closeList();o.push("<p>"+inline(l)+"</p>")}
    i++}
  closeList();return o.join("\n")}
async function init(){
  try{const r=await fetch("/api/processes");const d=await r.json();
    if(d.error)throw new Error(d.error);
    $("proc").innerHTML=d.processes.map(p=>`<option>${esc(p)}</option>`).join("")+"<option>ALL</option>";
    $("src").textContent="Input: "+(d.source.startsWith("http")?"Google Sheet (live)":d.source);
  }catch(e){$("proc").innerHTML="<option>Payment Processing</option>";$("src").textContent="Could not read processes: "+e.message}}
const LABEL={validate_input:"Validate input",apply_rules:"Apply rules",retrieve_evidence:"Retrieve evidence",external_research:"External research",llm_challenge:"LLM challenge",build_report:"Build report",finalize:"Finalize"};
const STXT={pending:"waiting",active:"running…",ok:"done",warn:"done (warning)",failed:"failed",skipped:"skipped"};
const INFO={
validate_input:["Validate input",["Reads the sheet filled in by the business owner: process, risk, loss events, loss amount, KRI, previous RCSA, control, applicable.","Checks that the required columns exist and the numbers are valid.","If the input is broken the run stops here and a failure report is still saved."]],
apply_rules:["Apply rules (deterministic)",["For every process-risk pair it checks loss events, loss amount, KRI, previous RCSA, control and the owner's applicability answer.","Loss events are compared with the KRI and with the control: loss but no KRI coverage, loss but control not effective, loss but marked not applicable, and so on (22-scenario matrix).","Output is flags only. No score, and a loss event is not treated as proof that a control failed."]],
retrieve_evidence:["Retrieve evidence",["For each flag it searches the local guidance in knowledge/ and picks the most relevant passages.","Every passage has a source id, so the report can cite where a challenge comes from."]],
external_research:["External research (Wikipedia + Tavily)",["Looks for public background and web sources about the process and its risks: Wikipedia for context, Tavily for current web results.","Each tool has a timeout and 3 retries. A failure is written to the run log, never hidden."]],
llm_challenge:["LLM challenge (OpenAI)",["The LLM writes challenge questions for the reviewer using the flags, the retrieved guidance and the external items.","The JSON answer is validated, unknown source ids are removed, and if the LLM fails a labelled deterministic fallback is used."]],
build_report:["Build report",["Assembles the RCSA Challenge Report in Markdown: summary, flags per risk, challenge questions, sources and the run status."]],
finalize:["Finalize",["Saves the report and the machine-readable run log.","Human Second Line review stays Pending. The agent never approves anything."]]};
const SUB={validate_input:"Reads the owner's sheet",apply_rules:"Loss events vs KRI vs control",retrieve_evidence:"Finds guidance to cite",external_research:"Wikipedia and web sources",llm_challenge:"Writes challenge questions",build_report:"Assembles the report",finalize:"Saves it, review stays Pending"};
let SEL=null,LAST=[];
function drawInfo(){
  const act=LAST.find(n=>n.status==="active");
  const name=SEL||(act&&act.name)||[...LAST].reverse().find(n=>n.status!=="pending")?.name||"validate_input";
  const n=LAST.find(x=>x.name===name)||{status:"pending",detail:""};const inf=INFO[name];if(!inf)return;
  $("info").innerHTML=`<h3>${esc(inf[0])} <span class="mut" style="font-weight:400">(${STXT[n.status]||""}${SEL?"":" · following live"})</span></h3><ul>${inf[1].map(t=>"<li>"+esc(t)+"</li>").join("")}</ul>`+
    (n.detail?`<div class="live"><strong>Result of this run:</strong> ${esc(n.detail)}</div>`:"")}
const COL={validate_input:["#7cc4ff","#1d5fd6"],apply_rules:["#ffc27a","#d9531e"],retrieve_evidence:["#7ff0cf","#0f9f86"],external_research:["#c9b6ff","#5b3fd1"],llm_challenge:["#ffb3d9","#c2307f"],build_report:["#fff0a8","#d99a00"],finalize:["#ffffff","#7d8bb0"]};
const BADGE={ok:"\u2713",warn:"!",failed:"\u2715",skipped:"\u2013"};
let BUILT=false,ORBS=[],SHIP_AT=-1,LASTH="";
function buildFlow(nodes){
  const f=$("flow");f.innerHTML="";ORBS=[];
  nodes.forEach(n=>{const d=document.createElement("div");d.className="pl pending";d.dataset.n=n.name;
    const c=COL[n.name]||["#fff","#888"];
    d.innerHTML=`<div class="ow${n.name==="llm_challenge"?" ring":""}" style="--c1:${c[0]};--c2:${c[1]}"><div class="orb"></div><div class="moon"></div><div class="bd"></div></div><div class="pn">${esc(LABEL[n.name]||n.name)}</div><div class="ps"></div><div class="sub">${esc(SUB[n.name]||"")}</div>`;
    d.onclick=()=>{SEL=(SEL===n.name)?null:n.name;drawFlow(LAST)};
    f.appendChild(d);ORBS.push(d)});
  BUILT=true}
function center(el){const s=$("stage").getBoundingClientRect(),r=el.querySelector(".orb").getBoundingClientRect();return{x:r.left-s.left+r.width/2,y:r.top-s.top+r.height/2,r:r.width/2}}
function placeShip(nodes){
  let idx=nodes.findIndex(n=>n.status==="active");
  if(idx<0){idx=0;nodes.forEach((n,i)=>{if(n.status!=="pending"&&n.status!=="skipped")idx=i})}
  const cs=ORBS.map(center);let h="";
  for(let i=1;i<cs.length;i++){const a=cs[i-1],b=cs[i];
    const prevDone=nodes[i-1].status!=="pending"&&nodes[i-1].status!=="active";
    const cls=nodes[i].status==="active"?"seg go":(prevDone&&nodes[i].status!=="pending"?"seg done":"seg");
    h+=`<line class="${cls}" x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}"/>`}
  if(h!==LASTH){$("orbits").innerHTML=h;LASTH=h}
  const to=cs[idx],from=cs[SHIP_AT<0?idx:SHIP_AT],ship=$("ship");
  if(idx!==SHIP_AT){const dx=to.x-from.x,dy=to.y-from.y;if(dx||dy)ship.style.setProperty("--rot",(Math.atan2(dy,dx)*180/Math.PI+45)+"deg")}
  ship.style.left=(to.x-to.r*0.9)+"px";ship.style.top=(to.y-to.r*1.05)+"px";SHIP_AT=idx}
function drawFlow(nodes){
  LAST=nodes;
  if(!BUILT||ORBS.length!==nodes.length)buildFlow(nodes);
  nodes.forEach((n,i)=>{const d=ORBS[i];d.className="pl "+n.status+(SEL===n.name?" sel":"");
    d.querySelector(".ps").textContent=STXT[n.status]||"";d.querySelector(".bd").textContent=BADGE[n.status]||""});
  placeShip(nodes);drawInfo()}
window.addEventListener("resize",()=>{LASTH="";if(LAST.length&&BUILT)placeShip(LAST)});
(function(){
  const c=$("stars"),x=c.getContext("2d");let W=0,H=0,shoot=null;
  const stars=[];for(let i=0;i<260;i++){let nx=Math.random(),ny;
    if(Math.random()<.5){ny=.85-.7*nx+(Math.random()-.5)*.3}else ny=Math.random();
    stars.push({x:nx,y:Math.min(1,Math.max(0,ny)),r:Math.random()*1.3+.2,p:Math.random()*6.28,s:.5+Math.random()*1.6})}
  function size(){const r=c.parentElement.getBoundingClientRect();W=c.width=Math.max(1,r.width);H=c.height=Math.max(1,r.height)}
  if(window.ResizeObserver)new ResizeObserver(size).observe(c.parentElement);size();
  function frame(t){
    if(c.offsetParent!==null){
      x.clearRect(0,0,W,H);
      const g=x.createLinearGradient(0,H,W,0);g.addColorStop(0,"rgba(130,110,255,0)");g.addColorStop(.5,"rgba(160,140,255,.13)");g.addColorStop(1,"rgba(130,110,255,0)");
      x.fillStyle=g;x.fillRect(0,0,W,H);x.fillStyle="#fff";
      for(const s of stars){x.globalAlpha=.3+.7*Math.abs(Math.sin(t/1000*s.s+s.p));x.beginPath();x.arc(s.x*W,s.y*H,s.r,0,6.283);x.fill()}
      x.globalAlpha=1;
      if(!shoot&&Math.random()<.006)shoot={x:Math.random()*W*.7,y:Math.random()*H*.35,l:0};
      if(shoot){x.strokeStyle="rgba(255,255,255,"+(1-shoot.l/40)+")";x.lineWidth=1.6;x.beginPath();x.moveTo(shoot.x,shoot.y);x.lineTo(shoot.x-28,shoot.y-12);x.stroke();shoot.x+=9;shoot.y+=4;if(++shoot.l>40)shoot=null}
    }
    requestAnimationFrame(frame)}
  requestAnimationFrame(frame)})();
let FOLLOWING=null;
function follow(id){
  if(FOLLOWING===id)return;FOLLOWING=id;
  const b=$("run");b.disabled=true;b.textContent="Running…";SEL=null;SHIP_AT=-1;
  $("result").style.display="none";$("reportcard").style.display="none";$("flowcard").style.display="";
  drawFlow(Object.keys(LABEL).map(k=>({name:k,status:"pending",detail:""})));
  const done=()=>{b.disabled=false;b.textContent="Run agent"};
  const fail=m=>{$("status").textContent="ERROR";$("status").className="pill bad";$("path").textContent=m;$("result").style.display="";done()};
  const tick=async()=>{
    try{
      const j=await (await fetch("/api/job/"+id)).json();
      drawFlow(j.nodes);$("timer").textContent=j.elapsed+" s";
      if(!j.finished){return setTimeout(tick,400)}
      if(j.error){return fail(j.error)}
      const d=j.result||{};
      const cls=d.status==="COMPLETED"?"ok":d.status==="FAILED"?"bad":"warn";
      $("status").textContent=d.status;$("status").className="pill "+cls;$("path").textContent=d.report_path||"";
      $("result").style.display="";
      if(d.report_markdown){$("report").innerHTML=md(d.report_markdown);$("reportcard").style.display=""}
      else if(d.error){$("report").innerHTML="<p class='bad'>"+esc(d.error)+"</p>";$("reportcard").style.display=""}
      done();
    }catch(e){fail(e.message)}};
  tick()}
$("run").onclick=async()=>{
  const b=$("run");b.disabled=true;
  try{
    const r=await fetch("/api/start",{method:"POST",headers:{"Content-Type":"application/json"},
      body:JSON.stringify({process:$("proc").value,use_llm:$("llm").checked,use_external:$("ext").checked})});
    const d=await r.json();if(!d.job)throw new Error(d.error||"could not start");follow(d.job);
  }catch(e){$("status").textContent="ERROR";$("status").className="pill bad";$("path").textContent=e.message;$("result").style.display="";b.disabled=false;b.textContent="Run agent"}};
// auto-follow: when n8n (or anything else) starts a run, the page shows it live
setInterval(async()=>{
  try{const j=await (await fetch("/api/latest")).json();
    if(j.job&&!j.finished&&j.job!==FOLLOWING)follow(j.job)}catch(e){}},1500);
init();
</script></body></html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"RCSA web app: http://localhost:{port}   (Ctrl+C to stop)")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
