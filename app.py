import streamlit as st
from github import Github
import os
import pandas as pd

token = st.secrets["github_token"]
g = Github(token)
repo = g.get_repo("Tim171717/test")

# New file content as string
new_content = "name,age\nAlice,25\nBob,30"

# Path to save it in the repo (can include folders)
file_path = "data.csv"

# Commit message
commit_message = "Add new data.csv from Streamlit app"

# Upload file (only if it doesn't already exist)
try:
    repo.create_file(path=file_path, message=commit_message, content=new_content, branch="main")
    st.success("File uploaded successfully!")
except Exception as e:
    st.error(f"Upload failed: {e}")
