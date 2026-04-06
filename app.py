import streamlit as st
import os
from pypdf import PdfReader

st.title("AI Study Assistant")

uploaded_pdf = st.file_uploader("Upload your PDF textbook", type="pdf")

question = st.text_input("Enter your question")

if uploaded_pdf:
    reader = PdfReader(uploaded_pdf)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    if question:
        if question.lower() in text.lower():
            st.write("Answer found in PDF:")
            st.write(text[:1000])
        else:
            st.write("Answer not found in the PDF.")