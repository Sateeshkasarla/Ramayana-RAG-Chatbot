from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks, embeddings):
    """
    Create a FAISS vector store from document chunks.
    """
    return FAISS.from_documents(chunks, embeddings)

def save_vectorstore(vectorstore, path="vector_db"):
    """
    Save the FAISS index locally.
    """
    vectorstore.save_local(path)

def load_vectorstore(embeddings, path="vector_db"):
    """
    Load an existing FAISS index.
    """
    # Try to load with the parameter, if it fails, try without it
    try:
        return FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True,
        )
    except TypeError:
        # If the parameter is not supported, load without it
        return FAISS.load_local(
            path,
            embeddings
        )