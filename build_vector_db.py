from utils.loader import load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model
from utils.vectorstore import create_vectorstore, save_vectorstore


def main():
    print("=" * 60)
    print("Building Ramayana Vector Database")
    print("=" * 60)

    print("\nLoading documents...")
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")

    print("\nSplitting documents...")
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    print("\nLoading embedding model...")
    embeddings = get_embedding_model()

    print("\nCreating FAISS vector database...")
    vectorstore = create_vectorstore(chunks, embeddings)

    print("\nSaving vector database...")
    save_vectorstore(vectorstore)

    print("\n✅ Vector database created successfully!")
    print("Location: vector_db/")


if __name__ == "__main__":
    main()