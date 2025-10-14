
import streamlit as st
from utils import get_sentiment, detect_crisis, build_prompt, load_tips, log_conversation
from ai_client import AIClient

st.set_page_config(page_title='Student AI — Mental Health Companion', layout='centered')
st.title('🧠 Student AI — Mental Health Companion Chatbot')
st.markdown('**Disclaimer:** This is a supportive companion, not a substitute for professional help.')

user_input = st.text_input("How are you feeling today?", placeholder="Type your thoughts here...")

if user_input:
    sentiment = get_sentiment(user_input)
    crisis = detect_crisis(user_input)
    if crisis:
        st.error("⚠️ Crisis language detected. Please reach out to emergency helpline or counselor.")
        st.info("Helpline: https://findahelpline.com | India: Dial 112")

    prompt = build_prompt(user_input, sentiment)
    with st.spinner("Thinking..."):
        try:
            client = AIClient()
            reply = client.chat(prompt)
        except Exception as e:
            reply = f"Error: {e}"

    st.subheader("💬 Chatbot Reply:")
    st.write(reply)
    log_conversation(user_input, reply, sentiment)

st.sidebar.title("Tips & Exercises")
for t in load_tips():
    st.sidebar.write("- " + t)
