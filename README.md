# 📖 Ramayana GPT – AI-Powered RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that enables users to interact with characters from the **Ramayana** such as **Lord Rama, Lakshmana, Hanuman, Sita, Ravana, and Vibhishana**.

The chatbot combines **Large Language Models (LLMs)** with **Retrieval-Augmented Generation (RAG)** to answer questions using trusted Ramayana documents while maintaining each character's unique personality.

---

# 🚀 Live Demo

🔗 **Live Application:**  
https://ramayana-rag-chatbot.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/Sateeshkasarla/Ramayana-RAG-Chatbot

---

# ✨ Features

- 🤖 AI-powered Ramayana chatbot
- 📚 Retrieval-Augmented Generation (RAG)
- 👑 Six Ramayana Characters
  - Lord Rama
  - Lakshmana
  - Hanuman
  - Devi Sita
  - Ravana
  - Vibhishana
- 🔍 FAISS Vector Search
- 🧠 LangChain Integration
- 📄 PDF Knowledge Base
- 💬 Persona-based Conversations
- 📖 Source Document References
- 🔐 Supports User API Keys
- ⚙️ Gemini & OpenAI Support
- 🎨 Modern Streamlit UI
- 📱 Responsive Layout

---

# 🏗 Project Architecture

```
                User
                  │
                  ▼
        Streamlit Web Application
                  │
        ┌─────────┴─────────┐
        │                   │
 Character Selection     API Key Validation
        │                   │
        └─────────┬─────────┘
                  ▼
           RAG Pipeline
                  │
         LangChain Retriever
                  │
         FAISS Vector Database
                  │
          Relevant Documents
                  │
          Prompt Engineering
                  │
       Gemini / OpenAI LLM
                  │
                  ▼
        Persona-based Response
```

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python     | Programming Language |
| Streamlit  | Web Application |
| LangChain  | RAG Framework |
| FAISS      | Vector Database |
| Google Gemini | Large Language Model |
| OpenAI GPT | Large Language Model |
| HuggingFace| Embeddings |
| PyPDF      | PDF Processing |
| dotenv     | Environment Variables |

---

# 📂 Project Structure

```
Ramayana-RAG-Chatbot
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   ├── Ramayana Educational...
│   ├── Shri-Ram-Charitmanas.pdf
│   └── valmiki_ramayanam.pdf
│
├
│
├── report/
│   ├── Architecture_Diagram.png
│   └── Project_Report.pdf
│
├── screenshots/
│   ├── Chatbot.png
│   ├── Chatbot1.png
│ 
│  
│
├── utils/
│   ├── api_validator.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── personas.py
│   ├── prompts.py
│   ├── rag.py
│   ├── splitter.py
│   └── vectorstore.py
│
├── vector_db/
│
├── app.py
├── build_vector_db.py
├── requirements.txt
├── runtime.txt
├── styles.css
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Sateeshkasarla/Ramayana-RAG-Chatbot.git

cd Ramayana-RAG-Chatbot
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

Example:

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

> The application also supports entering API keys directly from the sidebar without modifying the `.env` file.

---

# 📚 Build Vector Database

Run once:

```bash
python build_vector_db.py
```

This will:

- Load PDFs
- Split documents
- Create embeddings
- Build FAISS Vector Database

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 💬 Supported AI Providers

The chatbot supports multiple LLM providers.

## Google Gemini

- gemini-2.5-flash
- gemini-2.5-pro
- gemini-2.0-flash
- gemini-2.0-flash-lite

---

## OpenAI

- GPT-4.1
- GPT-4.1 Mini
- GPT-4o
- GPT-4o Mini

---

# 👑 Available Characters

| Character | Description |
|-----------|-------------|
| Lord Rama | Dharma, Leadership, Wisdom |
| Lakshmana | Loyalty, Duty |
| Hanuman | Devotion, Courage |
| Devi Sita | Compassion, Strength |
| Ravana | Knowledge, Ego |
| Vibhishana | Righteousness |

Each character has a dedicated persona prompt to maintain authentic conversational behavior.

---

# 🔍 RAG Workflow

1. User selects a character.
2. User asks a question.
3. Question is converted into embeddings.
4. FAISS retrieves relevant document chunks.
5. Context is combined with the selected persona prompt.
6. Gemini/OpenAI generates the answer.
7. Sources are displayed alongside the response.

---

# 📈 Future Improvements

- Voice Conversations
- Telugu Support
- Hindi Support
- Sanskrit Responses
- User Authentication
- Conversation Export
- Mobile Optimization
- Additional Ramayana Characters

---

# 👨‍💻 Developed By

**Kasarla Sateesh**

B.Tech – Computer Science Engineering

Email: sathishroyal967@gmail.com

GitHub: https://github.com/Sateeshkasarla

LinkedIn: *(Add your LinkedIn profile URL here)*

---

# 📄 License

This project is developed for educational and demonstration purposes.

---

# 🙏 Acknowledgements

- Google Gemini
- OpenAI
- LangChain
- FAISS
- Hugging Face
- Streamlit
- Valmiki Ramayana
- Shri Ram Charitmanas

---

⭐ If you found this project useful, consider giving the repository a star.