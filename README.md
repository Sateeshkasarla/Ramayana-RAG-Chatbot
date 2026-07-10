# 📖 Ramayana RAG Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-blue)

### AI-Powered Ramayana Knowledge Assistant using Retrieval-Augmented Generation (RAG)

**Developed by Kasarla Sateesh**

</div>

---

## Project Overview

The Ramayana RAG Chatbot is an AI-powered chatbot that answers questions from Ramayana documents using Retrieval-Augmented Generation (RAG). It combines LangChain, FAISS, HuggingFace embeddings, and Google Gemini 2.5 Flash to generate accurate, source-grounded answers.

## Features

- PDF and TXT document loading
- Automatic text chunking
- HuggingFace sentence embeddings
- FAISS vector database
- Google Gemini 2.5 Flash integration
- Persona-based responses (Rama, Lakshmana, Hanuman)
- Source citations
- Professional Streamlit interface

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.11 |
| UI | Streamlit |
| Framework | LangChain |
| Vector DB | FAISS |
| Embeddings | HuggingFace |
| LLM | Gemini 2.5 Flash |

## Folder Structure

```text
Ramayana-RAG-Chatbot/
├── app.py
├── build_vector_db.py
├── requirements.txt
├── styles.css
├── utils/
├── data/
├── vector_db/
├── screenshots/
├── report/
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
python build_vector_db.py
streamlit run app.py
```

## Workflow

1. Load documents
2. Split into chunks
3. Generate embeddings
4. Store in FAISS
5. Retrieve relevant chunks
6. Generate answer with Gemini
7. Display answer with sources

## Future Enhancements

- Voice input
- Multi-language support
- OCR support
- User authentication
- Conversation memory

## Author

**Kasarla Sateesh**

B.Tech CSE | AI Project
