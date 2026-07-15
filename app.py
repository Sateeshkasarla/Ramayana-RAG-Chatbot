# IMPORTANT: This must be the FIRST Streamlit command
from google import genai
from openai import OpenAI
from utils.api_validator import (
    validate_gemini_key,
    validate_openai_key,
)
import streamlit as st
st.set_page_config(
    page_title="Ramayana RAG Chatbot",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Now import other modules
from utils.rag import ask_question
from utils.personas import PERSONAS


# -----------------------------
# LOAD CSS
# -----------------------------
try:
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("styles.css not found. Using default styling.")

# -----------------------------
# SESSION STATE - Initialize all at once
# -----------------------------
if "initialized" not in st.session_state:
    st.session_state.character_chats = {
        "Rama": [],
        "Lakshmana": [],
        "Hanuman": [],
        "Sita": [],
        "Ravana": [],
        "Vibhishanudu": []
    }
    st.session_state.chat_history = []
    st.session_state.selected_persona = "Rama"
    st.session_state.processing = False
    st.session_state.input_processed = False
    st.session_state.initialized = True

# Get current state
persona = st.session_state.selected_persona
messages = st.session_state.character_chats[persona]

# -----------------------------
# CHARACTER IMAGES
# -----------------------------
CHARACTER_IMAGES = {
    "Rama": "👑",
    "Lakshmana": "🏹",
    "Hanuman": "🐒",
    "Sita": "🌸",
    "Ravana": "👹",
    "Vibhishanudu": "🛡️"
}

CHARACTER_NAMES = {
    "Rama": "Lord Rama",
    "Lakshmana": "Lakshmana",
    "Hanuman": "Hanuman",
    "Sita": "Devi Sita",
    "Ravana": "Ravana",
    "Vibhishanudu": "Vibhishanudu"
}

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("""
                 <div class="sidebar-title">
                📖 <span>Ramayana GPT</span>
                 </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    with st.container(border=True):

         st.markdown("## ⚙️ Model Configuration")

         provider = st.selectbox(
              "AI Provider",
              ["Gemini", "OpenAI"],
              key="provider"
         )

         if provider == "Gemini":

             api_key = st.text_input(
                 "Gemini API Key",
                 type="password",
                 key="gemini_api"
            )

             model_name = st.selectbox(
                 "Gemini Model",
                 [
                     "gemini-2.5-flash",
                     "gemini-2.5-pro",
                     "gemini-2.0-flash",
                     "gemini-2.0-flash-lite"
                 ]
           )

         else:

             api_key = st.text_input(
                 "OpenAI API Key",
                 type="password",
                 key="openai_api"
             )

             model_name = st.selectbox(
                 "OpenAI Model",
                 [
                     "gpt-4.1",
                     "gpt-4.1-mini",
                     "gpt-4o",
                     "gpt-4o-mini"
                 ]
             )
    st.session_state["model_name"] = model_name

    if api_key.strip():
        if provider == "Gemini":
            ok, message = validate_gemini_key(api_key.strip())
        else:
            ok, message = validate_openai_key(api_key.strip())

        if ok:
            st.success("✅ API Key Verified")

            st.session_state["user_api_key"] = api_key.strip()
            st.session_state["using_user_key"] = True

        else:
            st.error(f"❌ "+ message)

            st.session_state.pop("user_api_key", None)
            st.session_state["using_user_key"] = False

    else:
        st.session_state.pop("user_api_key", None)
        st.session_state["using_user_key"] = False
    

    if st.session_state.get("using_user_key", False):
       st.success("🔑 Using Your API Key")
    else:
       st.info(f"🔑 Using Default {provider} API Key")


    # Character selection
    st.markdown("### 👤 Choose Character")
    
    characters = ["Rama", "Lakshmana", "Hanuman", "Sita", "Ravana", "Vibhishanudu"]
    
    for char in characters:
        selected = char == persona

        if selected:
            st.markdown(
                """
                <style>
                div[data-testid="stButton"] > button[kind="primary"]{
                    background:linear-gradient(135deg,#2563EB,#1D4ED8) !important;
                    color:white !important;
                    border:none !important;
                    box-shadow:0 8px 18px rgba(37,99,235,.25);
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

        if st.button(
            f"{CHARACTER_IMAGES[char]}  {char}",
            key=f"btn_{char}",
            type="primary" if selected else "secondary",
            use_container_width=True,
        ):
            st.session_state.selected_persona = char
            st.rerun()

    st.markdown("---")
    
    # Chat History in Sidebar
    st.markdown("### 📜 Chat History")
    if st.session_state.chat_history:
        for i, (char, question) in enumerate(st.session_state.chat_history[-5:]):
            st.markdown(
                f"""
                <div style='background:rgba(255,255,255,0.05);padding:8px;border-radius:8px;margin:5px 0;font-size:12px;'>
                <b>{CHARACTER_IMAGES[char]} {char}:</b> {question[:30]}...
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.caption("No chat history yet")
        st.markdown("<p style='color:#94A3B8;font-size:14px;'>No chat history yet</p>", unsafe_allow_html=True)

    if st.button("🗑 Clear All Chats", use_container_width=True):
        # Clear every character chat
        for character in st.session_state.character_chats:
            st.session_state.character_chats[character] = []

        # Clear sidebar history
        st.session_state.chat_history = []

        st.session_state.processing = False

        st.rerun()
    # Clear current character chat
    if st.button("🗑 Clear Current Chat", use_container_width=True):
        st.session_state.character_chats[persona] = []
        st.session_state.processing = False
        st.rerun()

    st.markdown("---")
    st.markdown("### 🚀 Tech Stack")
    st.markdown(
        """
<div class="info-card">
✅ Gemini
</div>
<div class="info-card">
✅ LangChain
</div>
<div class="info-card">
✅ FAISS
</div>
<div class="info-card">
✅ HuggingFace
</div>
<div class="info-card">
✅ Streamlit
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        """
<div class="success-card">
✅ Vector Database Loaded
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.metric("📄 Documents", "1540")
    st.metric("🧩 Chunks", "4509")
    st.metric("🤖 Model", st.session_state.get("model_name", "Gemini 2.5 Flash"))
    # Push footer to bottom
    st.markdown(
           """
           <div style="height:60px;"></div>
           """,
           unsafe_allow_html=True,
        )

    st.markdown(
         """
    <div class="sidebar-footer">
        <div>© 2026</div>
        <div><strong>Developed by Kasarla Sateesh</strong></div>
        <div class="footer-tech">
            Powered by Gemini • LangChain • FAISS • Streamlit
        </div>
    </div>
    """,
    unsafe_allow_html=True,
    )

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="header-card">
<h1 class="main-title">
📖 Ramayana GPT
</h1>

<p class="sub-title">
Converse with Lord Rama, Hanuman, Sita, Lakshmana, Ravana and Vibhishana to explore the timeless wisdom of the Ramayana.
</p>
</div>
""", unsafe_allow_html=True
)

# Display current character
current_char = persona

st.markdown(
    f"""
    <div class="chat-header">
        <div class="chat-header-icon">
            {CHARACTER_IMAGES[current_char]}
        </div>
       <p>
        <div class="chat-header-title">
            Chatting with {CHARACTER_NAMES[current_char]}
        </div>
        <p>
    </div>
    """,
    unsafe_allow_html=True,
)
  
# -----------------------------
# DISPLAY CHAT HISTORY - Only once
# -----------------------------
for msg in messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style='display:flex;justify-content:flex-end;margin:10px 0;'>
                <div style='background:#2563EB;color:white;padding:16px 20px;
                border-radius:18px 18px 5px 18px;max-width:70%;
                box-shadow:0 4px 12px rgba(37,99,235,.25);'>
                {msg["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        char_icon = CHARACTER_IMAGES.get(persona, "🤖")
        char_name = CHARACTER_NAMES.get(persona, "Assistant")
        
        st.markdown(
            f"""
            <div style='display:flex;align-items:flex-start;margin:10px 0;'>
                <div style='font-size:40px;margin-right:12px;'>{char_icon}</div>
                <div style='flex:1;'>
                    <div style='font-weight:600;color:#16A34A;font-size:14px;margin-bottom:4px;'>
                        {char_name}
                    </div>
                    <div style='background:white;color:#111827;padding:18px 20px;
                    border-radius:18px 18px 18px 5px;max-width:70%;
                    border-left:5px solid #16A34A;
                    box-shadow:0 5px 18px rgba(0,0,0,.08);'>
                    {msg["content"]}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if "sources" in msg and msg["sources"]:
            shown = set()
            with st.expander(f"📚 Sources ({len(msg['sources'])})"):
                for doc in msg["sources"]:
                    source = doc.metadata.get("source", "Unknown")
                    page = doc.metadata.get("page", "N/A")
                    key = (source, page)
                    if key not in shown:
                        st.markdown(
                            f"""
                            <div class="source-card">
                            📄 **{source}**<br>
                            📑 Page: **{page}**
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        shown.add(key)

# -----------------------------
# EXAMPLE QUESTIONS
# -----------------------------
if len(messages) == 0:
    st.markdown("## 💡 Example Questions")
    
    example_questions = {
    "Rama": [
        "Why did you go into exile?",
        "What is the importance of Dharma?",
        "How did you defeat Ravana?",
        "What advice do you give for a righteous life?"
    ],

    "Lakshmana": [
        "Why did you accompany Rama to the forest?",
        "What was your role during the exile?",
        "Tell me about the Lakshmana Rekha.",
        "What did you learn from Lord Rama?"
    ],

    "Hanuman": [
        "How did you cross the ocean?",
        "How did you find Mother Sita?",
        "What made your devotion so strong?",
        "What message did you bring from Rama?"
    ],

    "Sita": [
        "How did you remain strong in Ashoka Vatika?",
        "What is true devotion?",
        "What inspired your courage?",
        "What message do you have for women today?"
    ],

    "Ravana": [
        "Why did you abduct Sita?",
        "What was your greatest strength?",
        "Do you regret your decisions?",
        "What lesson should people learn from your life?"
    ],

    "Vibhishanudu": [
        "Why did you leave Ravana?",
        "Why did you support Lord Rama?",
        "What is the value of righteousness?",
        "What advice do you have about choosing Dharma?"
    ]
}
    example_questions = example_questions.get(persona, [])
    cols = st.columns(2)
    for i, q in enumerate(example_questions):
        with cols[i % 2]:
            if st.button(q, use_container_width=True):
                st.session_state._question = q
                st.session_state.processing = False
                st.rerun()

# -----------------------------
# PROCESS QUESTION - Prevent duplicates
# -----------------------------

# Handle question from button
if "_question" in st.session_state:
    question = st.session_state._question
    del st.session_state._question
    # Add user message
    messages.append({"role": "user", "content": question})
    st.session_state.chat_history.append((persona, question))
    
    # Get response
    with st.chat_message("assistant"):
        answer, docs = ask_question(question, persona)

    # Add assistant response
    messages.append({
        "role": "assistant",
        "content": answer,
        "sources": docs
    })

    st.rerun()
# Handle chat input
question = st.chat_input(
    f"Ask {CHARACTER_NAMES[persona]} anything about the Ramayana..."
)
st.markdown(
    """
    <div style="
        text-align:center;
        color:#6B7280;
        font-size:13px;
        margin-top:6px;
        margin-bottom:8px;
    ">
    ⚠️ AI can make mistakes. Please verify important information with authentic Ramayana sources.
    </div>
    """,
    unsafe_allow_html=True,
)

if question and not st.session_state.input_processed:

    st.session_state.input_processed = True

    messages.append({
        "role": "user",
        "content": question
    })

    st.session_state.chat_history.append((persona, question))

    answer, docs = ask_question(question, persona)

    messages.append({
        "role": "assistant",
        "content": answer,
        "sources": docs
    })

    st.rerun()

if question is None:
    st.session_state.input_processed = False
