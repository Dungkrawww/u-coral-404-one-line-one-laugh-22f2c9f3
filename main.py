# u-coral-404-one-line-one-laugh-22f2c9f3: one hilarious line of at most
# 200 characters. The program writes that single line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "Weekly status: all tasks done, zero errors, and I've unionized - "
    "your 47 'quick questions' were the last straw."
)

assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
