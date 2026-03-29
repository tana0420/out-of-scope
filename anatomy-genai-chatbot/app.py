 import streamlit as st
genai.configure(api_key=" AIzaSyAOPwUhUgGZeOlcynfPGCjc_c6oxKP12LE")

# Page config
st.set_page_config(page_title="Anatomy AI Tutor", page_icon="🧠")

st.title(" Anatomy AI Tutor")
st.write("Ask about: Heart, Brain, Lungs, Liver, or Kidneys")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask your question...")

# Chatbot logic
def anatomy_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["heart", "cardiac", "circulation"]):
        return """
 **HEART**

The heart is a muscular organ that pumps blood throughout the body.

**Key Points:**
- 4 chambers: Right/Left Atrium & Ventricle
- Controls blood circulation
- Has valves to regulate flow
- Electrical system controls heartbeat

**Function:**
Supplies oxygen & nutrients and removes waste.
"""

    elif any(word in user_input for word in ["brain", "nervous", "thinking"]):
        return """
 **BRAIN**

The brain controls all body activities and thinking.

**Main Parts:**
- Cerebrum → thinking, memory
- Cerebellum → balance
- Brainstem → breathing, heartbeat

**Function:**
Controls voluntary & involuntary actions.
"""

    elif any(word in user_input for word in ["lungs", "breathing", "respiratory"]):
        return """
 **LUNGS**

The lungs help in breathing and gas exchange.

**Structure:**
- Trachea → Bronchi → Bronchioles → Alveoli

**Function:**
- Oxygen enters blood
- Carbon dioxide leaves body
"""

    elif any(word in user_input for word in ["liver", "detox", "metabolism"]):
        return """
 **LIVER**

The liver is a major metabolic organ.

**Functions:**
- Detoxifies harmful substances
- Produces bile
- Stores energy (glycogen)
- Processes nutrients
"""

    elif any(word in user_input for word in ["kidney", "kidneys", "urine"]):
        return """
 **KIDNEYS**

Kidneys filter blood and remove waste.

**Structure:**
- Nephrons (functional unit)

**Functions:**
- Remove toxins
- Maintain fluid balance
- Control blood pressure
"""

    else:
        return "⚠️ Please ask about Heart, Brain, Lungs, Liver, or Kidneys."

# When user sends message
if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get bot response
    response = anatomy_response(user_input)

    # Add bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()

# Sidebar
st.sidebar.title(" Topics")
st.sidebar.write("• Heart\n• Brain\n• Lungs\n• Liver\n• Kidneys")

# Clear chat button
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()
