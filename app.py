import streamlit as st
from github import Github
import os
import pandas as pd

token = st.secrets["github_token"]
g = Github(token)
repo = g.get_repo("yourusername/your-repo")
file = repo.get_contents("data.csv")
repo.update_file(file.path, "Updated data", new_content, file.sha)
