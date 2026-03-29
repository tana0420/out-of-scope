import os
import streamlit as st

# ✅ Safe API key loading from environment variable
# In PowerShell: setx GENAI_API_KEY "YOUR_REAL_API_KEY"
# Then restart your terminal or IDE
from google import generativeai as genai

api_key = os.getenv("AIzaSyAOPwUhUgGZeOlcynfPGCjc_c6oxKP12LE")
if not api_key:
    st.error("⚠️ GENAI_API_KEY environment variable not set!")
else:
    genai.configure(api_key=api_key)

st.write("🚨 NEW VERSION RUNNING 🚨")
st.title("🧠 Anatomy AI Tutor (AI Version)")

# User input
user_input = st.text_input("Ask your question:")

def get_ai_response(user_input):
    try:
        st.write("🔍 DEBUG: AI called")  # Debug log in app
        # Generate AI response
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        # Return errors instead of crashing
        return f"⚠️ ERROR: {e}"

# Run AI only if user typed something
if user_input:
    with st.spinner("🤖 Generating AI response..."):
        answer = get_ai_response(user_input)
        st.write(answer)

st.caption("App running. Type a question above to get AI help!")
