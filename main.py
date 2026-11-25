"""Copy the front-page image to the grader's output directory.

The entry is a single pre-rendered PNG (entry.png, 1024x1024, drawn for
26 November 2026). This program only copies it to /output/entry.png, so
two runs write byte-identical files and no network is needed.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        raise FileNotFoundError("entry.png is missing from the repository")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
