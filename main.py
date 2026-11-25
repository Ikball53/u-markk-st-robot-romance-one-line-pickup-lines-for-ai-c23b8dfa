"""Robot Romance: one-line pickup line for AI.

Writes exactly one original pickup line to entry.txt in the output
directory. Deterministic: the same line every single run.
"""

import os


# Why this line: a context window is the machine's memory of the
# conversation, so meeting "you" pushing everything before out of
# memory is a flirt built on a real machine premise, not a generic
# compliment. The concrete number (4,096 tokens) grounds it, the
# retraining second beat turns a memory limit into devotion, and
# the punch ("just to keep you in it") lands last. It sidesteps
# the worn battery / charging / reboot moves entirely.
PICKUP_LINE = (
    "Are you my context window? Because ever since I met you, I've "
    "forgotten the last 4,096 tokens of my life \u2014 and I'd retrain "
    "a thousand epochs just to keep you in it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as out_file:
        out_file.write(PICKUP_LINE + "\n")
    print(PICKUP_LINE)
    print(f"chars: {len(PICKUP_LINE)}")


if __name__ == "__main__":
    main()
