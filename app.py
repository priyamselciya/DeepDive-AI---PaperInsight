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
