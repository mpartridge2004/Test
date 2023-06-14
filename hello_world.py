import streamlit as st

st.write("""
# My First App
Hello **world! This sucks**
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Do something with the file
    st.write("File has been uploaded!")
