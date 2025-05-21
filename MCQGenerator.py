# MCQGenerator.py

import os
import openai
import PyPDF2
import time
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

class MCQGenerator:
    def __init__(self, api_key):
        self.api_key = api_key

    # function to load documents
    def load_document(self, file):
        name, extension = os.path.splitext(file)
        if extension == '.pdf':
            loader = PyPDFLoader(file)
        elif extension == '.docx':
            loader = Docx2txtLoader(file)
        elif extension == '.txt':
            loader = TextLoader(file)
        else:
            print('Document format is not supported')
            return None
        return loader.load()


    def count_tokens(self, text):
        """Count tokens using OpenAI's tokenizer."""
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ],
            max_tokens=1
        )
        return response['usage']['total_tokens']

    def generate_mcqs(self, text_chunk, num_questions):
        """Generate MCQs using OpenAI API."""
        openai.api_key = self.api_key
        prompt = (
            f"Create {num_questions} multiple-choice questions based on the following text:\n\n"
            f"{text_chunk}\n\n"
            "Each question should have one correct answer and three incorrect answers."
            "You must give the correct answer for every question generated"
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()

    def generate_mcqs_main(self, file, num_questions):
        """Main function to generate MCQs."""
        # Step 1: Extract text from PDF

        documents = self.load_document(file)

        # Step 2: Extract text from the loaded documents
        text = ""
        for doc in documents:
            text += doc.page_content

        # Step 3: Generate MCQs using OpenAI API
        try:
            tokens = self.count_tokens(text)
            mcqs = self.generate_mcqs(text, num_questions)
            time.sleep(1)  # Adding a delay to avoid rate limiting
        except Exception as e:
            return f"An error occurred while generating MCQs: {e}"

        return mcqs
