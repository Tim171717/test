import streamlit as st
from github import Github
import os
import pandas as pd

token = st.secrets["github_token"]
g = Github(token)
repo = g.get_repo("Tim171717/test")

df = pd.read_csv('Plan_U13A_2526HR.csv')
df['date'] = pd.to_datetime(df['date'])

    # Update rows where date matches
    df.loc[df['date'] == pd.to_datetime(date), 'selection'] = "['Prellen ', 'Duell um die Welt', 'Viereck passen - drei mal prellen für Punkt']"
    df.loc[df['date'] == pd.to_datetime(date), 'category'] = "['Technik', 'Technik', 'Spielfähigkeit']"
    df.loc[df['date'] == pd.to_datetime(date), 'catalog'] = 'U13A/Catalogs_U13A/Cat001.csv'

    # Convert DataFrame back to CSV string
    updated_content = df.to_csv(index=False)

    # Push the updated content back to GitHub
    repo.update_file(
        path=file_path,
        message=f"Updated {file_path} from Streamlit app",
        content=updated_content,
        sha=file.sha,
        branch="main"
    )

    st.success(f"{file_path} updated successfully!")
