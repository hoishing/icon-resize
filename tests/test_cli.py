import pytest
from subprocess import getstatusoutput
from pathlib import Path
from shutil import rmtree

# def setup_module(module):
#     print("-------------- setup before module --------------")
#     getstatusoutput("rm -rf test-output")


# def teardown_module(module):
#     print("-------------- teardown after module --------------")
#     getstatusoutput("rm -rf test-output")


def test_default():
    code, _ = getstatusoutput("icon-resize mic-512.png")
    assert code == 0
    for size in [256, 128, 64]:
        file = Path(f"mic-{size}.png")
        assert file.exists()
        file.unlink()


def test_output_folder():
    folder = "resized"
    code, _ = getstatusoutput(f"icon-resize mic-512.png --out-folder {folder}")
    assert code == 0

    assert Path(folder).exists()
    for size in [256, 128, 64]:
        file = Path(f"{folder}/mic-{size}.png")
        assert file.exists()
    rmtree(folder)
