"""The joke about the demo — make.fun bounty entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, 1-280 Unicode code points). No network, no
input, deterministic: the same joke every run.
"""

import os

JOKE = "My coding agent ran the demo, the app crashed, and it fixed the bug by deleting the demo."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
