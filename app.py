import streamlit as st
import subprocess
from pathlib import Path
import tempfile

st.title("LaTeX test")

if st.button("Start"):
    try:
        tex = r"""
\documentclass{article}
\begin{document}
Hello from Python.
\end{document}
"""

        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            tex_path = d / "example.tex"
            tex_path.write_text(tex)

            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", tex_path.name],
                cwd=d,
                capture_output=True,
                text=True,
                check=True
            )

            pdf_path = d / "example.pdf"
            st.success("Compilation succeeded")

            with open(pdf_path, "rb") as f:
                st.download_button(
                    "Download PDF",
                    f,
                    file_name="example.pdf",
                    mime="application/pdf"
                )

    except subprocess.CalledProcessError as e:
        st.error("LaTeX compilation failed")
        st.code(e.stdout)
        st.code(e.stderr)

    except Exception as e:
        st.error(str(e))
