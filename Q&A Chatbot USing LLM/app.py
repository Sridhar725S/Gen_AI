import streamlit as st
import cohere

# ✅ Directly use the API key (only for testing!)
cohere_api_key = "QzycWIpIZJi2YIBKdWJKsj8myKcRJtz6hdft7s2A"

# Check the key is set
if not cohere_api_key:
    raise ValueError("COHERE_API_KEY is missing. Set it directly or use a secure method.")

# Initialize Cohere client
co = cohere.Client(cohere_api_key)

# Function to get response from Cohere
def get_cohere_response(question):
    response = co.generate(
        model='command',  # Try 'command', 'command-light', etc., if needed
        prompt=question,
        max_tokens=100,
        temperature=0.5
    )
    return response.generations[0].text.strip()

# Streamlit setup
st.set_page_config(page_title="Q&A Demo")
st.header("Cohere-Powered Q&A App 💬🤖")

user_input = st.text_input("Ask me anything:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_cohere_response(user_input)
    st.subheader("The Response is:")
    st.write(response)
