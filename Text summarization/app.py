import streamlit as st
import cohere

# Paste your Cohere API key here
cohere_api_key = "QzycWIpIZJi2YIBKdWJKsj8myKcRJtz6hdft7s2A"
co = cohere.Client(cohere_api_key)

# Function to summarize text
def summarize_text(text):
    if len(text) < 250:
        return "⚠️ Text too short to summarize. Please enter at least 250 characters."
    
    response = co.summarize(
        text=text,
        length='medium',
        format='paragraph',
        model='command',
        temperature=0.3
    )
    return response.summary.strip()

# Streamlit UI
st.set_page_config(page_title="📝 Text Summarizer")
st.title("🧠 Cohere Text Summarizer")

input_text = st.text_area("Paste your long essay, blog post, or spicy drama 👇")

if st.button("Summarize it!"):
    if input_text.strip() == "":
        st.warning("Bro, don’t play games. Paste some actual text 😅")
    else:
        with st.spinner("Summoning the AI wizards... 🧙‍♂️✨"):
            summary = summarize_text(input_text)
            st.subheader("✨ Summary:")
            st.write(summary)
