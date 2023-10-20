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
        max_tokens=1000,
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content']

# Streamlit App
st.title("OpenAI Chat Assistant for Text Improvement")

uploaded_file = st.file_uploader("Upload a text file containing content guidelines", type="txt")

if uploaded_file is not None:
    guidelines = uploaded_file.read().decode("utf-8")
    st.write("Content Guidelines Loaded. Proceed to the chat.")
    
    user_input = st.text_area("You: ")
    
    if user_input:
        assistant_reply = chat_with_model(user_input, guidelines)
        st.write(f"Assistant: {assistant_reply}")
else:
    st.write("Please upload a text file to proceed.")
