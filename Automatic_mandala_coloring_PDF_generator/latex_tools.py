import os
import subprocess
import shutil

def create_latex_file(image_path, tex_output_path):
    """
    Format the mandala image on A4 page with minimal margins.
    """
    latex_code = r"""
\documentclass[a4paper]{article}
\usepackage[margin=1.5cm]{geometry}
\usepackage{graphicx}
\pagestyle{empty}
\begin{document}
\begin{center}
  \includegraphics[width=18cm,height=25cm,keepaspectratio]{%s}
\end{center}
\end{document}
    """ % image_path.replace("\\", "/")
    with open(tex_output_path, "w", encoding="utf-8") as f:
        f.write(latex_code)

def compile_latex_pdf(tex_file, workdir, pdf_output_path):
    """
    Compile the LaTeX file to PDF using pdflatex, save PDF to 'output'.
    """
    try:
        cmd = [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory", workdir,
            tex_file
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pdf_temp = os.path.join(workdir, os.path.splitext(os.path.basename(tex_file))[0] + ".pdf")
        shutil.move(pdf_temp, pdf_output_path)
        return True
    except Exception as e:
        print(f"[ERROR] pdflatex: {e}")
        return False