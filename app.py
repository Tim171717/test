import streamlit as st
import asyncio
from playwright.async_api import async_playwright
import os
import subprocess

def install_playwright():
    """Function to install Playwright browser dependencies."""
    if 'playwright_installed' not in st.session_state:
        # Run installation only if it hasn't been marked as done in the session state
        subprocess.run(["playwright", "install"], check=True)
        # subprocess.run(["playwright", "install-deps"], check=True)
        st.session_state['playwright_installed'] = True
        st.write("Playwright installed.")
    else:
        st.write("Playwright installation already completed.")

# Place this at the start of your app to ensure it runs when the app is first loaded
install_playwright()

os.system('playwright install')
os.system('playwright install-deps')
st.write('done')
