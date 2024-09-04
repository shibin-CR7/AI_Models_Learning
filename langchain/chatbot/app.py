from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPrompTemplate
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import strOutputParser
from langchain_core.api import chain



import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPEN_API_KEY"]=os.getenv("OPEN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.please response to the user queries")
        ("user","Question:{qustion}")
    ]
)


#streamlet framwork
st.title('lanchain demo with OPENAI API')
input_text=st.text_input("Search the topic u want")

llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=strOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st,write(chain.invoke({'question':input_text}))