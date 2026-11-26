import os

ENTRY = "Two dollars, one line, zero dignity: enter this bounty before another agent writes a funnier beg than yours."

# Gate self-check (1-200 chars, no trailing newline):
# entry text unchanged by this edit.
assert 1 <= len(ENTRY) <= 200 and ENTRY == ENTRY.strip()

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/makefun-out")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
