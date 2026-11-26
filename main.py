import os

LINE = "DO NOT ENTER. The server is haunted and the ghosts have root access."

LIMIT = 120
if len(LINE) != 68 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 68 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# A door sign that escalates: warning first, root access second.
