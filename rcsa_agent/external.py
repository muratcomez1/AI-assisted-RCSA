"""External research tools with timeout, retries, response validation and explicit status.

Nothing here raises: every call returns a dict with status ok / empty / failed / skipped,
so a failing tool is always visible in the run log and in the report (no silent failures).
"""
import json
import os
import re
import ssl
import time
import urllib.parse
import urllib.request

try:
    import certifi
    _CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:  # pragma: no cover
    _CTX = ssl.create_default_context()

RETRY_DELAY = 12.0  # GDELT asks for at most one request per ~5 seconds


def _http_json(url: str, data: dict | None = None, headers: dict | None = None, timeout: int = 15):
    body = json.dumps(data).encode("utf-8") if data is not None else None
    hdrs = {"User-Agent": "rcsa-agent/1.0", **(headers or {})}
    if body is not None:
        hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=hdrs)
    with urllib.request.urlopen(req, timeout=timeout, context=_CTX) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    return json.loads(raw)  # raises ValueError if the service answered with plain text


def _run_with_retries(tool: str, fn, attempts: int = 3) -> dict:
    last_error = ""
    for attempt in range(1, attempts + 1):
        try:
            items = fn()
            valid = [i for i in items if i.get("url") and i.get("title")]
            status = "ok" if valid else "empty"
            return {"tool": tool, "status": status, "attempts": attempt, "error": "", "items": valid}
        except Exception as exc:  # network, HTTP, JSON, schema
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < attempts:
                time.sleep(RETRY_DELAY)
    return {"tool": tool, "status": "failed", "attempts": attempts, "error": last_error, "items": []}


def gdelt_search(process: str, max_records: int = 5) -> dict:
    query = f'"{process}" (outage OR fraud OR incident OR fine OR breach) bank sourcelang:english'

    def call():
        params = urllib.parse.urlencode({
            "query": query, "mode": "ArtList", "maxrecords": max_records,
            "format": "json", "timespan": "6months", "sort": "DateDesc",
        })
        data = _http_json("https://api.gdeltproject.org/api/v2/doc/doc?" + params)
        arts = data.get("articles")
        if not isinstance(arts, list):
            raise ValueError("unexpected response: no 'articles' list")
        return [{"title": a.get("title", ""), "url": a.get("url", ""),
                 "snippet": f"{a.get('domain', '')} ({a.get('seendate', '')})"} for a in arts]

    return _run_with_retries("GDELT DOC API", call)


def wikipedia_search(process: str, max_results: int = 5) -> dict:
    """Wikipedia search API: free, no key, very stable. Gives background context on the process and its risks."""
    query = f"{process} operational risk"

    def call():
        params = urllib.parse.urlencode({
            "action": "query", "list": "search", "srsearch": query,
            "srlimit": max_results, "format": "json",
        })
        data = _http_json("https://en.wikipedia.org/w/api.php?" + params,
                          headers={"User-Agent": "rcsa-agent/1.0 (Ironhack bootcamp project)"})
        hits = (data.get("query") or {}).get("search")
        if not isinstance(hits, list):
            raise ValueError("unexpected response: no 'search' list")
        items = []
        for h in hits:
            title = h.get("title", "")
            snippet = re.sub(r"<[^>]+>", "", h.get("snippet", "") or "")
            items.append({"title": title,
                          "url": "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")) if title else "",
                          "snippet": snippet[:300]})
        return items

    return _run_with_retries("Wikipedia Search API", call)


def tavily_search(process: str, max_results: int = 5) -> dict:
    key = os.environ.get("TAVILY_API_KEY", "").strip()
    if not key:
        return {"tool": "Tavily Search API", "status": "skipped", "attempts": 0,
                "error": "TAVILY_API_KEY not set", "items": []}
    query = f"{process} operational risk incidents regulatory expectations banks"

    def call():
        data = _http_json("https://api.tavily.com/search",
                          data={"query": query, "max_results": max_results, "search_depth": "basic"},
                          headers={"Authorization": f"Bearer {key}"})
        results = data.get("results")
        if not isinstance(results, list):
            raise ValueError("unexpected response: no 'results' list")
        return [{"title": r.get("title", ""), "url": r.get("url", ""),
                 "snippet": (r.get("content", "") or "")[:300]} for r in results]

    return _run_with_retries("Tavily Search API", call)
