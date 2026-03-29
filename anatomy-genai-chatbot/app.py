  import streamlit as st
import google.generativeai as genai

# 🔑 ADD YOUR API KEY HERE
genai.configure(api_key="AIzaSyAOPwUhUgGZeOlcynfPGCjc_c6oxKP12LE")

model = genai.GenerativeModel("gemini-1.5-flash")

# Page config
st.set_page_config(page_title="Anatomy AI Tutor", page_icon="🧠")

st.title("🧠 Anatomy AI Tutor")
st.caption("💬 Ask anything about human anatomy")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask your question...")

# ✅ AI FUNCTION (NEW)
def get_ai_response(user_input):
    prompt = f"""
    You are a professional anatomy tutor.

    Explain in:
    - Simple language
    - Bullet points
    - Clear headings

    Question: {user_input}
    """
    response = model.generate_content(prompt)
    return response.text

# When user sends message
if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 🔥 THIS IS THE FIX (AI USED HERE)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_ai_response(user_input)
            st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

# Sidebar
st.sidebar.title("📚 Topics")
st.sidebar.write("""
• Heart  
• Brain  
• Lungs  
• Liver  
• Kidneys  
• Bones  
• Muscles  
• Nervous System  
""")

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()
