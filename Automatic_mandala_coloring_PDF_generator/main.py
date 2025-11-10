# main.py (updated prompts to include easy_mandala)
import sys
import os
import subprocess
import platform
import shutil
import json

OUTPUT_DIR = "output"
TMP_DIR = "tmp"
MANDALA_IMAGE = os.path.join(TMP_DIR, "mandala.png")
LATEX_FILE = os.path.join(TMP_DIR, "mandala.tex")
CONFIG_FILE = "config.json"

def get_os_type():
    os_name = platform.system()
    if os_name == "Windows":
        return "Windows"
    elif os_name == "Darwin":
        return "Mac"
    elif os_name == "Linux":
        try:
            with open("/etc/os-release") as f:
                text = f.read().lower()
                if "debian" in text or "ubuntu" in text:
                    return "Debian"
        except Exception:
            pass
        return "Linux"
    return "Unknown"

def print_install_instructions(component):
    os_type = get_os_type()
    print(f"\n[INSTRUCTIONS] How to install {component} on {os_type}:")
    if component == "Python":
        if os_type == "Windows":
            print("  choco install python3 -y")
        elif os_type == "Mac":
            print("  brew install python")
        elif os_type == "Debian":
            print("  sudo apt update && sudo apt install python3 python3-pip -y")
        else:
            print("Please refer to your system documentation for Python 3 installation.")
    elif component == "LaTeX":
        if os_type == "Windows":
            print("  choco install miktex -y")
        elif os_type == "Mac":
            print("  brew install --cask mactex")
        elif os_type == "Debian":
            print("  sudo apt install texlive-latex-base texlive-latex-extra -y")
        else:
            print("Please refer to your system documentation for LaTeX installation.")
    elif component == "Python Packages":
        if os_type == "Windows" or os_type == "Mac":
            print("  pip install matplotlib numpy")
        elif os_type == "Debian":
            print("  sudo apt install python3-numpy python3-matplotlib -y")
            print("Or use a virtual environment:")
            print("  python3 -m venv venv")
            print("  source venv/bin/activate")
            print("  pip install -r requirements.txt")
        else:
            print("Please refer to your system documentation for required Python packages.")

def check_python_packages():
    try:
        import matplotlib
        import numpy
    except ImportError:
        print("\n[ERROR] Required Python packages (matplotlib, numpy) are missing.")
        print_install_instructions("Python Packages")
        sys.exit(1)

def check_pdflatex():
    try:
        subprocess.run(["pdflatex", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except Exception:
        return False

def guide_latex_installation():
    print("\n[ERROR] LaTeX is not installed or 'pdflatex' is not available.")
    print_install_instructions("LaTeX")
    sys.exit(1)

def clean_temp_files():
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)

def ensure_dirs():
    os.makedirs(TMP_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_next_pdf_filename(output_dir):
    files = [f for f in os.listdir(output_dir) if f.startswith("output") and f.endswith(".pdf")]
    nums = []
    for f in files:
        basename = f.replace("output", "").replace(".pdf", "")
        try:
            nums.append(int(basename))
        except ValueError:
            pass
    idx = 1
    while idx in nums:
        idx += 1
    return f"output{idx}.pdf"

def ask_config_interactive():
    print("\n--- MANUAL CONFIGURATION ---")
    print("Example configuration:")
    print('{"color_hint_mode": "number", "color_mode": "advanced", "batch_count": 2, "mandala_style": "easy_mandala", "mandala_max_radius": 1.42}\n')

    color_hint_mode = input("How do you want coloring hints? [none/name/number]: ").strip().lower()
    if color_hint_mode not in ["none", "name", "number"]:
        color_hint_mode = "none"

    color_mode = input("Which color list to use? [basic/advanced] (example: advanced): ").strip().lower()
    if color_mode not in ["basic", "advanced"]:
        color_mode = "basic"

    batch_count_input = input("How many PDFs to generate? (number, example: 2): ").strip()
    batch_count = int(batch_count_input) if batch_count_input.isdigit() else 1

    mandala_style = input("Mandala style? [random/geometric/easy_mandala] (example: easy_mandala): ").strip().lower()
    if mandala_style not in ["random", "geometric", "easy_mandala"]:
        mandala_style = "random"

    mandala_max_radius = 1.35
    if mandala_style == "geometric" or mandala_style == "easy_mandala":
        radius_input = input("Max radius for geometric/easy mandala? (example: 1.42, recommended: 1.35-1.48): ").strip()
        try:
            mandala_max_radius = float(radius_input)
        except Exception:
            mandala_max_radius = 1.35

    config = {
        "color_hint_mode": color_hint_mode,
        "color_mode": color_mode,
        "batch_count": batch_count,
        "mandala_style": mandala_style,
        "mandala_max_radius": mandala_max_radius
    }
    return config

def save_config_json(config, path="config.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

def load_config_json(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def convert_legacy_config(config):
    # Convert legacy config to new config style
    if "color_hint_mode" not in config:
        if "write_color_names" in config:
            color_hint_mode = "name" if config["write_color_names"] else "none"
        else:
            color_hint_mode = "none"
        config["color_hint_mode"] = color_hint_mode
    return config

def main():
    print("=== AUTOMATIC MANDALA COLORING PDF GENERATOR ===")
    print("[INFO] Checking Python packages...")
    check_python_packages()
    print("[INFO] Checking for pdflatex...")
    if not check_pdflatex():
        guide_latex_installation()

    if os.path.exists(CONFIG_FILE):
        print(f"[INFO] Configuration found in {CONFIG_FILE}.")
        config = load_config_json(CONFIG_FILE)
    else:
        config = ask_config_interactive()
        save_config_json(config, CONFIG_FILE)
        print(f"[INFO] Configuration saved in {CONFIG_FILE}.")

    config = convert_legacy_config(config)

    from mandala_generator import generate_mandala_image
    from latex_tools import create_latex_file, compile_latex_pdf

    batch_count = config.get("batch_count", 1)
    color_hint_mode = config.get("color_hint_mode", "none")
    color_mode = config.get("color_mode", "basic")
    mandala_style = config.get("mandala_style", "random")
    mandala_max_radius = config.get("mandala_max_radius", 1.35)

    print(f"[INFO] Generating {batch_count} PDF(s)...")

    for i in range(batch_count):
        ensure_dirs()
        print(f"[INFO] Generating mandala {i+1}/{batch_count}...")
        legend = None
        # generate_mandala_image will return legend if color_hint_mode == "number"
        legend = generate_mandala_image(
            MANDALA_IMAGE,
            color_hint_mode=color_hint_mode,
            color_mode=color_mode,
            mandala_style=mandala_style,
            mandala_max_radius=mandala_max_radius
        )
        create_latex_file(MANDALA_IMAGE, LATEX_FILE, legend=legend)
        pdf_filename = get_next_pdf_filename(OUTPUT_DIR)
        pdf_output = os.path.join(OUTPUT_DIR, pdf_filename)
        print(f"[INFO] Compiling PDF with LaTeX ({pdf_filename})...")
        success = compile_latex_pdf(LATEX_FILE, TMP_DIR, pdf_output)

        if success:
            print(f"[SUCCESS] PDF generated and saved to {pdf_output}")
        else:
            print("[ERROR] Something went wrong during LaTeX compilation.")

        clean_temp_files()

    print("[DONE] You can find the final PDFs in the 'output/' folder.")

if __name__ == "__main__":
    main()