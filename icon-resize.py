#!/usr/bin/env python3

import typer, re
from pathlib import Path
from subprocess import getoutput
from typer import Argument, Option
import platform


def main(
    src_image: str = Argument(..., help="path to source image"),
    sizes: str = Option(
        "256,128,64", help="output sizes, comma seperated eg. 512,256,128"
    ),
    out_folder: str = Option(
        "", help="output folder path, default same as source file"
    ),
):
    src = Path(src_image)
    sizes_arr = sizes.split(",")
    name_arr = re.split(r"(\d+)", src.name)
    name = name_arr[0] if len(name_arr) > 1 else src.stem
    for size in sizes_arr:
        file_name = name + size + src.suffix
        out_file = (
            Path(out_folder) / file_name if out_folder else src.with_name(file_name)
        )
        if platform.system() == "Darwin":
            # getoutput(f"sips -Z {size} -o {out_file} {src}")
            # getoutput(f"optipng {out_file}")
            # else:
            getoutput(f"convert {src} -resize {size}x{size} {out_file}")
        print("output:", out_file)


if __name__ == "__main__":
    typer.run(main)
