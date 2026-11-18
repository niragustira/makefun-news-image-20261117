"""One image summing up Tuesday 17 November 2026's world news.

This program takes the editorial collage stored next to it and writes it
to the output location as entry.png. It performs no network access and
always writes identical bytes, so repeated runs reproduce the same file.

The collage is a newspaper front page dated TUESDAY 17 NOVEMBER 2026 with
four panels, each picturing one of the day's big stories:

  1. The Kerch Bridge to Crimea is struck by Ukraine and a road span
     falls, while Russia hits bridges over the Dnipro in Kyiv.
  2. Tankers are hit by mines near the Strait of Hormuz as a third US
     aircraft carrier reaches the Middle East.
  3. Trump lands in Manila for the ASEAN summit, and a three-way
     Xi-Trump-Putin meeting is confirmed for Thursday in Shenzhen.
  4. A ULA Vulcan rocket fails in flight and 40 Amazon Leo internet
     satellites are lost.

The output directory comes from the MAKEFUN_OUTPUT environment variable
when set, and defaults to /output otherwise.
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"


def output_path() -> Path:
    directory = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    return directory / IMAGE_NAME


def main() -> None:
    source = Path(__file__).resolve().parent / IMAGE_NAME
    if not source.is_file():
        raise FileNotFoundError(f"missing image next to main.py: {source}")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
