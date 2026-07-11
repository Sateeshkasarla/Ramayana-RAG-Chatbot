# IMPORTANT: This must be the FIRST Streamlit command
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
    st.markdown(
        "<div class='sidebar-title'>📖 Ramayana RAG</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Character selection
    st.markdown("### 👤 Choose Character")
    
    characters = ["Rama", "Lakshmana", "Hanuman", "Sita", "Ravana", "Vibhishanudu"]
    
    for char in characters:
        button_type = "primary" if char == persona else "secondary"
        if st.button(
            f"{CHARACTER_IMAGES[char]} {char}",
            key=f"btn_{char}",
            type=button_type,
            use_container_width=True,):
            if st.session_state.selected_persona != char:
                st.session_state.selected_persona = char
                st.rerun()

    st.markdown("---")
    
    # Clear conversation
    if st.button("🗑 Clear Conversation", use_container_width=True):
        st.session_state.character_chats[persona] = []
        st.session_state.chat_history = []
        st.session_state.processing = False
        st.rerun()
    
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
        st.markdown("<p style='color:#94A3B8;font-size:14px;'>No chat history yet</p>", unsafe_allow_html=True)
    
    if st.button("🗑 Clear All History", use_container_width=True):
        st.session_state.chat_history = []
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
    st.metric("🤖 Model", "Gemini 2.5 Flash")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="header-card">
<h1 class="main-title">
📖 Ramayana RAG Chatbot
</h1>
<p class="sub-title">
Explore the wisdom of the Ramayana using <b>Retrieval-Augmented Generation (RAG)</b>.
</p>
</div>
""", unsafe_allow_html=True)

# Display current character
current_char = persona
st.markdown(
    f"""
    <div style='background:linear-gradient(135deg,#1E293B,#0F172A);
    padding:15px 20px;border-radius:15px;margin:10px 0 20px 0;
    border-left:5px solid #FCD34D;'>
    <span style='font-size:28px;'>{CHARACTER_IMAGES[current_char]}</span>
    <span style='color:white;font-size:22px;font-weight:600;margin-left:12px;'>
    Chatting with {CHARACTER_NAMES[current_char]}
    </span>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
with col1:
    st.info("📚 **1540 Documents Loaded**")
with col2:
    st.success("⚡ Gemini 2.5 Flash")
with col3:
    st.warning("⚡ FAISS Vector Search")

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
                    <div style='background:white;padding:18px 20px;
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
            with st.expander(f"📚 Sources ({len(shown)})"):
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
    
    example_questions = [
        "Why did you go into exile, Lord Rama?",
        "Hanuman, how did you cross the ocean?",
        "Sita, what gave you strength in Ashoka Vatika?",
        "Ravana, why did you abduct Sita?"
    ]
    
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
    print("APP RERUN")


# Handle chat input
question = st.chat_input(
    f"Chat with {CHARACTER_NAMES[persona]}..."
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
# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("© 2026 | Developed by Kasarla Sateesh | Powered by Gemini • LangChain • FAISS • Streamlit")