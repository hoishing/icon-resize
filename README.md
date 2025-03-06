# Icon Resize

[![ruff-badge]][ruff] [![pypi-badge]][pypi-url] ![MIT] [![uv-badge]][uv]

![screenshot](https://i.imgur.com/K00hCxN.png)

> CLI to create lossless icons in multiple sizes

[mit]: https://img.shields.io/github/license/hoishing/icon-resize

## Features

- resize icon file(png/jpg) to multiple sizes
- lossless compression for png files
- maintain aspect ratio and transparency

## Prerequisite

- macOS or Linux (Windows not tested)
- python3.10+
- [Image Magick][magick] `brew install imagemagick`

## Installation

`pip install icon-resize`

## Usage

```shell
# default resize to 256, 128, 64
icon-resize mic-512

# specify resize to 128, 64
icon-resize mic-512 --sizes "128,64"

# save to 'mic' folder with default sizes
icon-resize mic-512 --out-folder mic/

# enable autocomplete in current session
eval "$(_ICON_RESIZE_COMPLETE=zsh_source icon_resize)"
```

## Technical Details

- use [Typer][typer] for CLI and help docs generation
- use [Image Magick][magick] for both resize and compress images

## Questions?

Open a [github issue] or ping me on [X]

[github issue]: https://github.com/hoishing/icon-resize-cli/issues
[magick]: https://imagemagick.org
[pypi-badge]: https://img.shields.io/pypi/v/icon-resize
[pypi-url]: https://pypi.org/project/icon-resize/
[ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff]: https://github.com/astral-sh/ruff
[typer]: https://typer.tiangolo.com
[uv-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json
[uv]: https://docs.astral.sh/uv/
[X]: https://x.com/intent/tweet?text=https://github.com/hoishing/gllm/%20%0D@hoishing
