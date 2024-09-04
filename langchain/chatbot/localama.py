from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["OPEN_API_KEY"]=os.getenv("OPEN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages (
    [
        ("system","you are a helpful assistant.please response to the user queries")
        ("user","Question:{qustion}")
]
)  


st.title('lanchain demo with OPENAI API')
input_text=st.text_input("Search the topic u want")

llm=Ollama(model="llama2")
output_parser=strOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))