import requests
import streamlit as st

# Define a function to get essay response
def get_essay_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={'input': {'topic': input_text}}
        )
        response.raise_for_status()
        return response.json().get('output', {}).get('content', 'No content received')
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Define a function to get poem response
def get_poem_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={'input': {'topic': input_text}}
        )
        response.raise_for_status()
        return response.json().get('output', 'No output received')
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Streamlit application
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_essay_response(input_text))

if input_text1:
    st.write(get_poem_response(input_text1))






