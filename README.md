# DeepDive AI - PaperInsight

## Overview
**DeepDive AI - PaperInsight** is a Retrieval-Augmented Generation (RAG) application designed to help users extract insights from AI research papers. Users can upload PDFs, ask questions, and receive precise answers based on the document content.

## Features
- 📄 **Upload Multiple PDFs**: Users can upload AI research papers in PDF format.
- 🔍 **Semantic Search**: Retrieves the most relevant sections based on user queries.
- 🤖 **AI-Powered Answers**: Generates answers using OpenAI's GPT-3.5 model.
- 🏗 **FAISS-Based Indexing**: Efficient document search with FAISS.
- 📌 **Relevant Section Highlights**: Displays key parts of the paper used to generate answers.

## Tech Stack
- **Python**
- **Streamlit** - Interactive web UI
- **FAISS** - Vector search for semantic retrieval
- **Sentence Transformers** - Text embedding generation
- **OpenAI GPT-3.5** - AI-powered response generation
- **PyPDF2** - PDF text extraction

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Install Required Packages
```sh
pip install streamlit openai faiss-cpu sentence-transformers PyPDF2 numpy
```

### Run the Application
```sh
streamlit run app.py
```

## How It Works
1. **Upload PDFs**: Select one or multiple research papers.
2. **Ask Questions**: Enter a query related to the uploaded paper.
3. **Retrieve Answers**: The system finds relevant text and generates an AI-powered response.
4. **View Relevant Sections**: The retrieved document snippets used to generate the response are displayed.

## Environment Variables
To use OpenAI API, set up your API key:
```sh
export OPENAI_API_KEY='your-api-key-here'  # Linux/macOS
set OPENAI_API_KEY='your-api-key-here'  # Windows
```
Alternatively, enter it directly in the Streamlit UI.

## Folder Structure
```
DeepDive-AI-PaperInsight/
├── app.py  # Main Streamlit app
├── requirements.txt  # List of dependencies
├── README.md  # Project documentation
```

## Future Enhancements
- 🔹 **Support for more file formats (e.g., DOCX, TXT)**
- 🔹 **Improved text chunking using NLP techniques**
- 🔹 **Fine-tuning models for domain-specific insights**

## License
This project is licensed under the **MIT License**.

## Contributors
Developed by **PRIYAM SELCIYA**. Feel free to contribute and enhance the project!

---
🚀 **DeepDive AI - PaperInsight: Making AI Research More Accessible!**

