# MCQnA Generator from a Custom Document using Generative AI

## 📘 Introduction

Generative AI represents a transformative advancement in artificial intelligence, utilizing deep learning models to create content that mimics human intelligence. This application leverages the power of Large Language Models (LLMs) such as GPT-3.5 turbo, GPT-4, and GPT-4o mini from OpenAI to automate question creation and answer generation from user-provided documents.

It is designed to support educators, students, and content creators by generating meaningful multiple-choice questions (MCQs) and descriptive answers from materials like PDFs, Word documents, or plain text files.

---

## 🎯 Objectives

1. Accept PDF, Word, or Text files as input.
2. Generate:
   - MCQs with 4 options and the correct answer
   - Descriptive answers to user queries based on the document
3. Evaluate and compare GPT-3.5 turbo, GPT-4, and GPT-4o mini, and deploy the best-performing model.

---

## 🧠 Methodology

The system is divided into two modules:

- **QnA Module**: Accepts a user question and responds with a concise, document-relevant answer using LLMs.
- **MCQ Generation Module**: Analyzes the input document and generates MCQs along with the correct choice.

Both modules use OpenAI's API through Langchain for robust prompt engineering and response handling.

---

## 🧰 Requirements

### Software

- Python 3.x
- Libraries:
  - `openai`
  - `langchain`
  - `streamlit`
- Development Tools: VSCode / PyCharm / Google Colab

### Hardware

- Processor: Intel i5 or better
- RAM: 8 GB or more

---

## 💡 Innovation / Contribution

The **MCQnA Generator** automates the creation of multiple-choice and descriptive questions from textual input. By transforming unstructured content into interactive learning tools, this project:

- Saves time for educators and learners
- Demonstrates the potential of LLMs in EdTech
- Encourages personalized and adaptive learning

---

## 📦 Project Structure

```bash
MCQnA-Generator/
├── app.py                 # Streamlit app
├── mcq_generator.py       # MCQ generation logic
├── qna_generator.py       # QnA logic
├── utils.py               # Helper functions
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
└── sample_docs/           # Sample input files (PDF/Doc/Text)

```
---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/deepakgoudasirsi/MCQnA-Generator.git
   cd email-guardian-ai
   ```
---

## Contact
Deepak Gouda - [@deepakgoudasirsi](https://github.com/deepakgoudasirsi)
Project Link: [https://github.com/deepakgoudasirsi/MCQnA-Generator](https://github.com/deepakgoudasirsi/MCQnA-Generator)
