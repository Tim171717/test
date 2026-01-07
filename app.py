import streamlit as st
import asyncio
from playwright.async_api import async_playwright
import os
import subprocess
import subprocess
from pathlib import Path

if st.button("Start"):
    try:
        tex = r"""
        \documentclass{article}
        \begin{document}
        Hello from Python.
        \end{document}
        """

        path = Path("example.tex")
        path.write_text(tex)

        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", path.name],
            check=True
        )

    except Exception as e:
        print(Exception)
