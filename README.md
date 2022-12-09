# Icon Resize CLI

![screenshot](https://i.imgur.com/K00hCxN.png)

[![GitHub](https://img.shields.io/github/license/hoishing/icon-resize)](https://opensource.org/licenses/MIT)

> CLI to create lossless icons in multiple sizes

## Features

- resize icon file(png/jpg) to multiple sizes
- lossless compression for png files
- maintain aspect ratio and transparency

## Requirements

- macOS or Linux
- python3.10+
- [Typer][typer] `pip install "typer[all]"`
- macOS
  - [optipng][optipng] `brew install optipng`
- Linux
  - [Image Magick][magick] `brew install imagemagick`

## Usage

```shell
# display help
python3 icon-resize.py --help

# create icons with default sizes(256, 128 and 64) in current folder
python3 icon-resize.py <icon-file>

# create icons with specific sizes in current folder
python3 icon-resize.py --sizes 512,256,128 <icon-file>

# create icons with specific sizes and destination folder
python3 icon-resize.py --sizes 1024,512 --out-folder ~/Downloads <icon-file>
```

## Technical Details

🔗 [source code](https://github.com/hoishing/icon-resize)

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
