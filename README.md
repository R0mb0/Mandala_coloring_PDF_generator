# Automatic Mandala Coloring PDF Generator

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6665a99c29b14b87bddd3ac553c13bf9)](https://app.codacy.com/gh/R0mb0/Mandala_coloring_PDF_generator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/R0mb0/Batch_PDF_OCR_Processor)
[![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/R0mb0/Batch_PDF_OCR_Processor)
[![Donate](https://img.shields.io/badge/PayPal-Donate%20to%20Author-blue.svg)](http://paypal.me/R0mb0)

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]](https://creativecommons.org/licenses/by-nc-sa/4.0)

Generate beautiful, printable mandalas for coloring, perfectly formatted as PDFs for A4 paper.  
All layout, margins, and centering are handled automatically.

---

## Preview

<div align="center">

[![preview](https://github.com/R0mb0/Mandala_coloring_PDF_generator/blob/main/ReadMe_Imgs/Mandala.png)](https://github.com/R0mb0/Mandala_coloring_PDF_generator/tree/main/Example_images)

</div>

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

---

### Linux (Debian/Ubuntu)

```sh
sudo apt update
sudo apt install python3 python3-pip texlive-latex-base texlive-latex-extra -y
```

---

### Windows

Install [Chocolatey](https://chocolatey.org/install) (Windows package manager), then:

```sh
choco install python3 -y
choco install miktex -y
```

#### **Common pip issues on Windows**

If after installing Python via Chocolatey `pip` does **not work** or is **not found**, follow these steps:

1. **Check if pip is available:**
    ```sh
    where pip
    ```
    If no result, pip is not installed or not in PATH.

2. **Try running pip via Python:**
    ```sh
    python -m pip --version
    ```
    If this shows an error, pip is likely missing.

3. **Manual pip installation:**
    - Download the official [get-pip.py](https://bootstrap.pypa.io/get-pip.py) script and save it to your computer.
    - Open a Command Prompt in the folder where you saved the script.
    - Run:
      ```sh
      python get-pip.py
      ```
    - This will install pip.

4. **Add pip to PATH (if still not found):**
    - Locate where pip was installed, typically in:
      ```
      C:\Users\<YOUR_USER>\AppData\Local\Programs\Python\Python3x\Scripts\
      ```
    - Add this folder to your system's PATH:
      - Open "Edit environment variables" in Windows.
      - Add the above path to the `PATH` variable and restart the Command Prompt.

5. **Test pip:**
    ```sh
    pip --version
    ```
    or
    ```sh
    python -m pip --version
    ```

If you still have issues, pip can always be used with the `python -m pip ...` syntax!

---

### Mac

Install [Homebrew](https://brew.sh/) (Mac package manager), then:

```sh
brew install python
brew install --cask mactex
```

---

### Python packages

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
"color_hint_mode": "number",
"color_mode": "advanced",
"batch_count": 2,
"mandala_style": "geometric",
"mandala_max_radius": 1.32
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
- **Windows pip issue:** See the detailed guide in the Windows installation section above.

---

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
