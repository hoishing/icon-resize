# Icon Resize CLI

![py-badge] [![black-badge]][black-url] ![mit]

![screenshot](https://i.imgur.com/K00hCxN.png)

> CLI to create lossless icons in multiple sizes

🔗 [source code](https://github.com/hoishing/icon-resize)

[mit]: https://img.shields.io/github/license/hoishing/icon-resize
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[py-badge]: https://img.shields.io/badge/python-3.10%20%7C%203.11-blue

## Features

- resize icon file(png/jpg) to multiple sizes
- lossless compression for png files
- maintain aspect ratio and transparency

## Requirements

- macOS or Linux
- python3.10+
- [Typer][typer] `pip install "typer[all]"`
- [Image Magick][magick] `brew install imagemagick`

## Usage

- clone the repo `git clone https://github.com/hoishing/icon-resize`
- install the env with [poetry] `poetry install`
- start the env `poetry shell`

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

### macOS

- use built-in `sips` to resize images
- use [optipng][optipng] to compress png files

Choosing `sips` + `optipng` because they provide better compression then `Image Magick` in general without parameters tuning.

### Linux

- use [Image Magick][magick] for both resize and compress images

## Need Help?

Open a [github issue](https://github.com/hoishing/icon-resize/issues) or ping me on [Twitter](https://twitter.com/hoishing) ![](https://api.iconify.design/logos/twitter.svg?width=20)

[typer]: https://typer.tiangolo.com
[optipng]: https://formulae.brew.sh/formula/optipng
[magick]: https://imagemagick.org
[poetry]: https://python-poetry.org/
