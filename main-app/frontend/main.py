import streamlit as st
import requests


st.title("File Uploader")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    with st.spinner("Uploading..."):
        response = requests.post("http://localhost:8000/load-document", files=files)
        if response.status_code == 200:
            st.success("File uploaded successfully!")
        else:
            st.error(f"Upload failed: {response.text}")