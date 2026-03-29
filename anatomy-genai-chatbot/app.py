import streamlit as st
st.write("🚨 NEW VERSION RUNNING 🚨")
import google.generativeai as genai

# 🔑 PUT YOUR REAL API KEY HERE
genai.configure(api_key="AIzaSyAOPwUhUgGZeOlcynfPGCjc_c6oxKP12LE")

model = genai.GenerativeModel("gemini-pro")

st.title("🧠 Anatomy AI Tutor (AI Version)")

user_input = st.text_input("Ask your question:")

def get_ai_response(user_input):
    try:
        st.write("🔍 DEBUG: AI CALLED")

        response = model.generate_content(user_input)

        return response.text
    except Exception as e:
        return f"ERROR: {e}"

if user_input:
    answer = get_ai_response(user_input)
    st.write(answer)
