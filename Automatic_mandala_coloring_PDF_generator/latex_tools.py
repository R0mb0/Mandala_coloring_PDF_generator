import os
import subprocess
import shutil
import math

def create_latex_file(image_path, tex_output_path, legend=None):
    """
    Format the mandala image on A4 page with minimal margins.
    If legend is given, place it in bottom left, horizontal table, max 5 columns, then go to next row.
    """
    latex_code = r"""
\documentclass[a4paper]{article}
\usepackage[margin=1.5cm]{geometry}
\usepackage{graphicx}
\usepackage{array}
\usepackage{float}
\pagestyle{empty}
\begin{document}
\begin{center}
  \includegraphics[width=18cm,height=25cm,keepaspectratio]{%s}
\end{center}
""" % image_path.replace("\\", "/")

    if legend:
        # Max 5 columns per row
        max_col = 5
        n_items = len(legend)
        n_rows = math.ceil(n_items / max_col)

        # Prepare rows
        rows = []
        for i in range(n_rows):
            row = legend[i*max_col:(i+1)*max_col]
            rows.append(row)

        # Build tabular format string
        col_format = "|c|c|" * max_col

        latex_code += r"""
\vspace{2em}
\begin{flushleft}
\begin{minipage}{0.98\linewidth}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{%s}
""" % col_format

        # Header row (only for first row)
        header_cells = []
        for _ in range(max_col):
            header_cells.extend([r"\textbf{No.}", r"\textbf{Color Name}"])
        latex_code += " & ".join(header_cells) + r"\\ \hline" + "\n"

        # Data rows
        for row in rows:
            row_cells = []
            for cell in row:
                row_cells.extend([str(cell[0]), cell[1]])
            # Fill empty cells if needed
            missing = max_col*2 - len(row_cells)
            row_cells.extend([""]*missing)
            latex_code += " & ".join(row_cells) + r"\\ \hline" + "\n"

        latex_code += r"""\end{tabular}
\end{minipage}
\end{flushleft}
"""
    latex_code += r"\end{document}\n"
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