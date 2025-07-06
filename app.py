import streamlit as st
from github import Github
import os
import pandas as pd

token = st.secrets["github_token"]
g = Github(token)
repo = g.get_repo("Tim171717/test")
file = repo.get_contents("Plan_U13A_2526HR.csv")
st.write(file)
repo.update_file(file.path, "Updated data", new_content, file.sha)
