import streamlit as st
import cohere

# 🔑 Your Cohere API Key
COHERE_API_KEY = "QzycWIpIZJi2YIBKdWJKsj8myKcRJtz6hdft7s2A"

co = cohere.Client(COHERE_API_KEY)

st.set_page_config(page_title="Text-to-Text with Cohere", layout="centered")
st.header("🧠 Text to Text App (Cohere)")

prompt_input = st.text_area("Enter your prompt:")

submit = st.button("Generate")

if submit and prompt_input:
    response = co.generate(
        model='command',
        prompt=prompt_input,
        max_tokens=300,
        temperature=0.7
    )
    st.subheader("✍️ Response:")
    st.write(response.generations[0].text.strip())
