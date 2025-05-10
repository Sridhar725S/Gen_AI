import streamlit as st
from gtts import gTTS
import cohere
from io import BytesIO

# Initialize Cohere
co = cohere.Client("QzycWIpIZJi2YIBKdWJKsj8myKcRJtz6hdft7s2A")  # Replace with your real API key

st.set_page_config(page_title="Cohere + Voice", layout="centered")
st.title("🧠 Text-to-Text + 🎤 Text-to-Speech")

# Get text input from user
user_prompt = st.text_area("Enter a prompt for Cohere to respond:")

if st.button("Generate and Speak"):
    if user_prompt.strip():
        # 1. Generate text using Cohere
        response = co.generate(
            model="command-r-plus",
            prompt=user_prompt,
            max_tokens=300,
            temperature=0.7
        )
        output_text = response.generations[0].text.strip()

        st.subheader("🧠 Cohere Says:")
        st.write(output_text)

        # 2. Convert to speech
        tts = gTTS(output_text)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # 3. Play audio
        st.subheader("🎧 Hear It Out")
        st.audio(mp3_fp, format="audio/mp3")
    else:
        st.warning("Yo! You gotta give me something to work with 😅")
