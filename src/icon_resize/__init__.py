#!/usr/bin/env python3

import re
import typer
from pathlib import Path
from subprocess import STDOUT, check_output, getstatusoutput
from typer import Argument, Option


def main(
    src_image: str = Argument(..., help="path to source image"),
    sizes: str = Option(
        "256,128,64", help="output sizes, comma separated eg. 512,256,128"
    ),
    out_folder: str = Option(
        "", help="output folder path, default same as source file"
    ),
):
    """resize icon / image with diff sizes"""
    check_imagemagick_installed()

    src = Path(src_image)
    sizes_arr = sizes.split(",")
    name_arr = re.split(r"(\d+)", src.name)
    name = name_arr[0] if len(name_arr) > 1 else src.stem
    for size in sizes_arr:
        file_name = name + size + src.suffix
        out_file = src.with_name(file_name)
        if out_folder:
            out_folder = Path(out_folder)
            out_folder.mkdir(parents=True, exist_ok=True)
            out_file = out_folder / file_name
        code, output = getstatusoutput(f"magick {src} -resize {size}x{size} {out_file}")
        if code != 0:
            raise Exception(output)

        print("resized:", out_file)


def check_imagemagick_installed():
    try:
        # Run the "magick --version" command in Windows
        check_output(["magick", "--version"], stderr=STDOUT)
    except FileNotFoundError:
        # If neither command is found, ImageMagick is not installed
        return False
    # If the command runs successfully, ImageMagick is installed
    return True


def entry():
    typer.run(main)


if __name__ == "__main__":
    entry()
