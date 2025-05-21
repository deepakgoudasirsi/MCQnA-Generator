# app.py

import streamlit as st
from dotenv import load_dotenv, find_dotenv
from MCQGenerator import MCQGenerator
from QA import QA
import os
import tempfile

# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)

# Streamlit UI
st.title("MCQnA GENERATOR")
file = st.file_uploader("Upload a PDF/Word/Text file", type=["pdf", "docx", "txt"])
action = st.selectbox("Do you want to create MCQ or ask anything about the content?", ["Select", "MCQ", "QA"])

if file and action != "Select":
    # Save the uploaded file to a temporary file
    file_extension = file.name.split('.')[-1]  # Extract the file extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_extension}') as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name

    api_key = os.getenv('OPENAI_API_KEY')
    if action == "MCQ":
        num_questions = st.number_input("Enter the number of questions to be generated:", min_value=1, step=1)
        if st.button("Generate MCQs"):
            mcq_generator = MCQGenerator(api_key)
            with st.spinner("Generating MCQs..."):
                mcqs = mcq_generator.generate_mcqs_main(temp_file_path, num_questions)
                st.write(mcqs)
    elif action == "QA":
        question = st.text_input("Ask anything about the content of your file:")
        if st.button("Get Answer") and question:
            qa = QA(api_key)
            with st.spinner("Generating Answer..."):
                answer = qa.qa_main(temp_file_path, question)
                st.write(f'Answer: {answer}')
