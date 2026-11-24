#!/usr/bin/env python3
"""Two Days of Quiet Dread — one code review comment approving a PR
with quiet existential dread (max 140 characters).

The laugh comes from the dread itself: everything checks out, the reviewer
approves anyway, and entropy gets the last word."""

import os

LINE = "LGTM. It passes CI, the diff is small, and entropy wins eventually. Merging anyway."

assert LINE.strip(), "entry must not be empty"
assert "\n" not in LINE, "entry must be a single line"
assert len(LINE) <= 140, f"entry too long: {len(LINE)} chars (max 140)"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)}-char entry to /output/entry.txt")
