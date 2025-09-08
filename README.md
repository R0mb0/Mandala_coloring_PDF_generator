# Automatic Mandala Coloring PDF Generator

Generate beautiful, printable mandalas for coloring, perfectly formatted as PDFs for A4 paper.  
All layout, margins, and centering are handled automatically.

---

## Features

- **Perfect PDF layout for A4:** Mandalas are always centered and never cropped.
- **Customizable styles:** Choose between random motifs or geometric (classical) mandalas.
- **Color names:** Optionally print a color name inside every closed area (helpful for kids/learning).
- **Batch generation:** Easily produce multiple unique mandalas in a single run.
- **Windows, Mac, Linux support** via automatic dependency checks and install guides.
- **Simple configuration** via `config.json`; interactive setup if the file is missing.
- **Clean output:** Only PDFs are kept; all temporary files are wiped after each run.

---

## Installation

### 1. Dependencies

- **Python 3**
- **LaTeX** (pdflatex)
- **Python packages:** matplotlib, numpy

#### Linux (Debian/Ubuntu)

```sh
sudo apt update
sudo apt install python3 python3-pip texlive-latex-base texlive-latex-extra -y
```

#### Windows

Install [Chocolatey](https://chocolatey.org/install) (Windows package manager), then:

```sh
choco install python3 -y
choco install miktex -y
```

#### Mac

Install [Homebrew](https://brew.sh/) (Mac package manager), then:

```sh
brew install python
brew install --cask mactex
```

#### Python packages

```sh
pip install -r requirements.txt
```

---

## Usage

1. Place all project files in the same folder.
2. Edit (or create) your `config.json` for custom settings (see below).
3. Run the generator:

```sh
python main.py
```

4. Find your PDFs in the `output/` folder.

---

## Configuration

All options are set in `config.json`.  
If the file is missing, the script will ask you for all settings interactively.

Example:

```json
{
    "write_color_names": true,
    "color_mode": "advanced",
    "batch_count": 3,
    "mandala_style": "geometric",
    "mandala_max_radius": 1.42
}
```

See [`config-parameters.md`](config-parameters.md) for a full description of each option.

---

## Expected Behavior

- **PDFs are always perfectly formatted for A4 paper**, with a large square mandala centered.
- **No cropping, no layout errors.**
- **If you want color names inside each area, set `write_color_names` to true.**
- **Choose style (`random` or `geometric`) and color list (`basic` or `advanced`) freely.**
- **You can generate as many PDFs as you want with one run.**
- **If you run the script with no config file, you’ll be prompted to enter every option.**

---

## Troubleshooting

- **Missing dependencies:** The script will show install instructions for your OS.
- **LaTeX errors:** Make sure `pdflatex` is installed and in your PATH.
- **Images not centered:** Check your LaTeX installation and make sure you're using the latest version of the code.

---

## Support

Open an issue on GitHub or contact the author for help, suggestions, or feature requests!
