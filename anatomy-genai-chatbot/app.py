

import streamlit as st
from google import generativeai as genai

# -----------------------------
# Configure your API key
# -----------------------------
genai.configure(api_key="AIzaSyBnCRKW5cK5HyUat3Q2XVDf834afhk15Lk")  # Replace with your API key

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="🧠 Anatomy AI Tutor",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Anatomy AI Tutor 🤖")
st.sidebar.markdown("""
Ask questions about **human anatomy** and get **AI explanations**.  

**Tips:**  
- Ask step-by-step questions  
- Keep questions specific  

💡 Your chat history is saved while the app is open.
""")

# -----------------------------
# Sidebar: Pick bubble colors
# -----------------------------
user_color = st.sidebar.color_picker("Pick your chat color (You)", "#FFD8A8")
ai_color = st.sidebar.color_picker("Pick AI chat color", "#D8B4FE")

# -----------------------------
# Initialize chat history
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Choose a working model
# -----------------------------
AVAILABLE_MODEL = "gemini-3-flash-preview"

# -----------------------------
# User input
# -----------------------------
st.title("🧠 Anatomy AI Tutor")
user_input = st.text_input("Ask a question:")

# -----------------------------
# Function to get AI response
# -----------------------------
def get_ai_response(question):
    try:
        model = genai.GenerativeModel(AVAILABLE_MODEL)
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"⚠️ ERROR: {e}"

# -----------------------------
# Handle user input
# -----------------------------
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    answer = get_ai_response(user_input)
    st.session_state.history.append({"role": "assistant", "content": answer})

# -----------------------------
# Display chat history with left/right alignment
# -----------------------------
for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(
            f"""
            <div style='display:flex; justify-content:flex-end; margin:5px 0'>
                <div style='background-color:{user_color}; padding:10px; border-radius:10px; max-width:70%'>
                    <strong>🧍 You:</strong> {chat['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='display:flex; justify-content:flex-start; margin:5px 0'>
                <div style='background-color:{ai_color}; padding:10px; border-radius:10px; max-width:70%'>
                    <strong>🤖 AI:</strong> {chat['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# Scrollable chat container
# -----------------------------
st.markdown(
    """
    <style>
    div[data-testid="stVerticalBlock"] {
        max-height: 600px;
        overflow-y: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
