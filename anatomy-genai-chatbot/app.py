import streamlit as st
import google.generativeai as genai

# 🔑 PASTE YOUR REAL API KEY HERE
API_KEY = "AIzaSyAOPwUhUgGZeOlcynfPGCjc_c6oxKP12LE"

# Configure Gemini
genai.configure(api_key=API_KEY)

# Try stable model
model = genai.GenerativeModel("gemini-pro")

# Page setup
st.set_page_config(page_title="Anatomy AI Tutor", page_icon="🧠")

st.title("🧠 Anatomy AI Tutor")
st.caption("💬 Ask anything about human anatomy")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask your question...")

# ✅ DEBUG AI FUNCTION
def get_ai_response(user_input):
    try:
        st.write("🔍 DEBUG: Function called")
        st.write(f"🔍 DEBUG: User input → {user_input}")

        if not API_KEY or API_KEY == "PASTE_YOUR_REAL_API_KEY_HERE":
            return "❌ ERROR: API key not added!"

        st.write("🔍 DEBUG: Calling Gemini API...")

        response = model.generate_content(user_input)

        st.write("🔍 DEBUG: Response received")

        if hasattr(response, "text") and response.text:
            return response.text
        else:
            return "⚠️ ERROR: Empty response from AI"

    except Exception as e:
        return f"❌ ERROR: {e}"

# Handle input
if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking..."):
            reply = get_ai_response(user_input)
            st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

# Sidebar
st.sidebar.title("📚 Topics")
st.sidebar.write("""
• Heart ❤️  
• Brain 🧠  
• Lungs 🫁  
• Liver 🧬  
• Kidneys 🧪  
• Bones 🦴  
• Muscles 💪  
""")

# Clear chat
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()
