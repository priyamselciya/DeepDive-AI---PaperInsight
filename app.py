import streamlit as st
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import openai
import os
# Set up OpenAI API key
openai.api_key = "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"  # Replace with your OpenAI API key
# Load Sentence Transformer model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
# Initialize FAISS index
dimension = 384  # Dimension of the embeddings
index = faiss.IndexFlatL2(dimension)
import PyPDF2
import os

def extract_text_from_pdfs(file_paths):
    """Extracts text from multiple PDF files in a local environment."""
    extracted_text = {}

    for file_path in file_paths:
        if not os.path.exists(file_path):  # Check if file exists
            extracted_text[file_path] = f"❌ File not found -> {file_path}"
            continue

        try:
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
                extracted_text[file_path] = text[:1000]  # Limit output to first 1000 chars for preview
        except Exception as e:
            extracted_text[file_path] = f"⚠️ Error reading {file_path}: {str(e)}"

    return extracted_text

# ✅ **Fixed file path list with commas and raw strings**
pdf_files = [
    r"D:\project\1706.03762v7.pdf",
    r"D:\project\2501.12948v1.pdf",
    r"D:\project\2312.11805v4.pdf",
    r"D:\project\2407.21783v3.pdf",
    r"D:\project\2303.08774v6.pdf"
]  # Replace with actual file paths

# 🔍 Extract text from PDFs
pdf_texts = extract_text_from_pdfs(pdf_files)

# 📄 Print the extracted text for each file
for file, text in pdf_texts.items():
    print(f"\n📂 **Text from {file}:**\n{text}\n")
# Function to preprocess text into chunks
def preprocess_text(text, chunk_size=500):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks
    # Function to generate embeddings and build FAISS index
def build_faiss_index(chunks):
    chunk_embeddings = model.encode(chunks)
    index.add(np.array(chunk_embeddings))
    return index
    # Function to perform semantic search
def semantic_search(query, index, chunks, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    relevant_chunks = [chunks[i] for i in indices[0]]
    return relevant_chunks
    # Function to generate response using OpenAI GPT-3.5
def generate_response(query, context):
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()
    import streamlit as st

# Streamlit app function
def main():
    st.title("Research Paper Q&A with RAG")
    st.write("Upload a research paper (PDF) and ask questions!")

    # File upload widget in Streamlit
    uploaded_file = st.file_uploaderr(r"D:\project\1706.03762v7.pdf",
    r"D:\project\2501.12948v1.pdf",
    r"D:\project\2312.11805v4.pdf",
    r"D:\project\2407.21783v3.pdf",
    r"D:\project\2303.08774v6.pdf"
)
  # Replace with actual file paths", type="pdf")

    if uploaded_file is not None:
        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)

        # Preprocess the extracted text into chunks
        chunks = preprocess_text(text)

        # Build FAISS index with the text chunks
        build_faiss_index(chunks)

        # User query input
        query = st.text_input("Enter your question:")

        if query:
            # Perform semantic search to find relevant chunks
            relevant_chunks = semantic_search(query, index, chunks)

            # Combine the relevant chunks to form context
            context = " ".join(relevant_chunks)

            # Generate response using OpenAI GPT-3.5
            response = generate_response(query, context)

            # Display the response
            st.write("**Answer:**")
            st.write(response)

            # Optionally, display the relevant sections (chunks) used to generate the answer
            st.write("**Relevant Sections:**")
            for i, chunk in enumerate(relevant_chunks):
                st.write(f"Chunk {i + 1}:")
                st.write(chunk)

# Run the app (Local environment)
if __name__ == "__main__":
    main()
