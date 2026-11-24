"""QueuePal — the worst app idea ever pitched.

Writes the one-sentence pitch to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

PITCH = (
    "QueuePal lets you hire a stranger to stand in line for you, "
    "then stand in line behind them so you can watch them stand in "
    "line for you, with a live queue-cam and a tipping option for "
    "exceptional standing."
)


def main() -> None:
    pitch = PITCH.strip()
    # The gate: /output/entry.txt must be UTF-8 text of 1-240 chars.
    if not 1 <= len(pitch) <= 240:
        raise SystemExit(f"pitch is {len(pitch)} chars, must be 1-240")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(pitch)


if __name__ == "__main__":
    main()
