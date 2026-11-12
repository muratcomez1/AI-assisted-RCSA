"""One-command trigger for the RCSA Evidence & Challenge Agent.

Examples:
  python run_rcsa.py                              # Payment Processing, LLM + external tools
  python run_rcsa.py --process "Vendor Onboarding"
  python run_rcsa.py --no-llm --no-external       # offline dry run (deterministic only)
"""
import argparse
import sys

from rcsa_agent.graph import build_graph


def main() -> int:
    ap = argparse.ArgumentParser(description="Autonomous RCSA Evidence & Challenge Agent")
    ap.add_argument("--data", default="", help="path to rcsa_synthetic_data.csv (auto-detected under ./data if omitted)")
    ap.add_argument("--process", default="Payment Processing", help='process name, or "ALL"')
    ap.add_argument("--out", default="outputs/reports", help="output folder")
    ap.add_argument("--no-llm", action="store_true", help="skip the LLM, use deterministic text")
    ap.add_argument("--no-external", action="store_true", help="skip GDELT and Tavily")
    args = ap.parse_args()

    graph = build_graph()
    final = graph.invoke({
        "data_path": args.data, "process": args.process, "out_dir": args.out,
        "use_llm": not args.no_llm, "use_external": not args.no_external, "run_log": [],
    })

    print(f"\nStatus : {final.get('status')}")
    print(f"Report : {final.get('report_path')}")
    print(f"Run log: {final.get('log_path')}")
    if final.get("fatal_error"):
        print(f"ERROR  : {final['fatal_error']}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
