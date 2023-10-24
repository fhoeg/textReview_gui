import os
import streamlit as st
import openai
from dotenv import load_dotenv

def load_guidelines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
def save_guidelines(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)
openai.api_key = api_key

def chat_with_model(prompt, guidelines):
    messages = [
        {"role": "system", "content": guidelines},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": ""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=1536,
        messages=messages,
        temperature=0,
        stream=True
    )
    return response['choices'][0]['message']['content']

# Load Guidelines from a file
guidelines_path = "system.txt"  # Replace with your file path
guidelines = load_guidelines(guidelines_path)

# Streamlit App
st.title("OpenAI Chat Assistant for Text Improvement")

with st.expander("Guidelines ein-/ausblenden"):
    guidelines = st.text_area("Content Guidelines:", guidelines)
    if st.button("Speichern"):
        save_guidelines(guidelines_path, guidelines)

# st.write("Bitte geben Sie Ihr Textbeispiel ein.")

user_input = st.text_area("Bitte geben Sie Ihr Textbeispiel ein.")

if user_input:
    assistant_reply = chat_with_model(user_input, guidelines)
    st.write(f"Assistant: {assistant_reply}")
