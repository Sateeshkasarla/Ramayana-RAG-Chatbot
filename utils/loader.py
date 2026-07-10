from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)


def load_documents(data_folder="data"):
    """
    Load all supported documents from the data folder.

    Supported formats:
    - PDF
    - TXT
    - DOCX

    Returns:
        List of LangChain Document objects.
    """

    documents = []

    data_path = Path(data_folder)

    for file in data_path.iterdir():

        if file.suffix.lower() == ".pdf":

            loader = PyPDFLoader(str(file))
            docs = loader.load()

            # Add metadata
            for doc in docs:
                doc.metadata["source"] = file.name
                doc.metadata["page"] = doc.metadata.get("page", "N/A")

            documents.extend(docs)

        elif file.suffix.lower() == ".txt":

            loader = TextLoader(str(file), encoding="utf-8")
            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = file.name
                doc.metadata["page"] = "N/A"

            documents.extend(docs)

        elif file.suffix.lower() == ".docx":

            loader = Docx2txtLoader(str(file))
            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = file.name
                doc.metadata["page"] = "N/A"

            documents.extend(docs)

    return documents