# QA.py

import openai
import os
import time
import tiktoken
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter


class QA:
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

    # function to chunk data
    def chunk_data(self, data, chunk_size=256, chunk_overlap=20):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(data)

    # function to create embeddings
    def create_embedding(self, chunks):
        embeddings = OpenAIEmbeddings(api_key=self.api_key)
        vector_store = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
        vector_store.persist()
        return vector_store

    # function to ask questions and get answers
    def ask_and_get_answer(self, vector_store, q, k=3):  # q: input question, search answer from the vector store
        """Retrieves relevant document chunks and answers the question."""
        retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': k})
        docs = retriever.get_relevant_documents(q)

        # Extract text from retrieved docs
        retrieved_texts = [doc.page_content.strip() for doc in docs if doc.page_content.strip()]
        print(retrieved_texts)

        # If no relevant chunks are found, return a default response
        if not retrieved_texts:
            return "I am sorry, could not find it in the document."

        # Concatenate retrieved texts to pass only document-based context
        context = "\n\n".join(retrieved_texts)

        # Use LLM only with retrieved context
        llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1, api_key=self.api_key)
        prompt = (f"Answer the question based on the document below:\n\n{context}\n\nQuestion: {q}\nAnswer:"
                  f"If the question is not relevant to the document, ALWAYS give the response as 'I am sorry, could not find relevant context in the document'")

        response = llm.predict(prompt)
        return response


    # function to calculate embedding cost
    def calculate_embedding_cost(self, chunks):
        enc = tiktoken.encoding_for_model('text-embedding-ada-002')
        total_tokens = sum([len(enc.encode(page.page_content)) for page in chunks])
        embedding_cost = total_tokens / 1000 * 0.0004
        return total_tokens, embedding_cost

    def qa_main(self, file, question):
        """Main function for Q&A."""
        data = self.load_document(file)
        if data:
            chunks = self.chunk_data(data)
            tokens, embedding_cost = self.calculate_embedding_cost(chunks)
            vector_store = self.create_embedding(chunks)
            answer = self.ask_and_get_answer(vector_store, question)
            # time.sleep(1)       # Adding a delay to avoid rate limiting
            return answer