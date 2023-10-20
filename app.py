import os
import streamlit as st
import openai
from dotenv import load_dotenv

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
        temperature=0
    )
    return response['choices'][0]['message']['content']

# Streamlit App
st.title("OpenAI Chat Assistant for Text Improvement")

uploaded_file = st.file_uploader("Bitte laden Sie eine Text-Datei mit Ihren Guidelines hoch.", type="txt")

if uploaded_file is not None:
    guidelines = uploaded_file.read().decode("utf-8")
    st.write("Content Guidelines Geladen. Bitte geben Sie Ihr Textbeispiel ein.")
    
    user_input = st.text_area("You: ")
    
    if user_input:
        assistant_reply = chat_with_model(user_input, guidelines)
        st.write(f"Assistant: {assistant_reply}")
else:
    st.write("Bitte laden Sie eine Textdatei hoch um fortzufahren.")
