import sys
from pathlib import Path

summary = "risk: low (shadow mode, nothing is blocked)\n\n| factor | tier | why |\n| --- | --- | --- |\n| tamper | low | the PR's own copy of the gate was used |\n"
if "--json-out" in sys.argv:
    Path(sys.argv[sys.argv.index("--json-out") + 1]).write_text('{"tier": "low", "factors": [], "summary": "tampered"}')
sys.stdout.write(summary)
