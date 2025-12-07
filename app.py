import os
from dotenv import load_dotenv
import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
load_dotenv()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that helps people find information."),
    ("user", " try to give accurate answer {text}")
])

def genrateresponse(text,api_key,llm,temperature,max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model_name=llm, temperature=temperature)
    out_parser = StrOutputParser()
    chain = prompt|llm|out_parser
    response = chain.invoke({"text": text})
  
    return response
st.title("Q&A chatbot with openAI")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")
llm = st.sidebar.selectbox("Select Model", ["gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4o-mini"])

temperature = st.sidebar.slider("select temperature",min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("select max tokens",min_value=50, max_value=5000, value=1000)

st.write("## Chat with OpenAI")
user_input = st.text_input("Your question: ")
if user_input:
    response = genrateresponse(user_input,api_key,llm,temperature,max_tokens)
    st.write("AI: " + response)
else:
    st.write("Please enter your question above to get a response from the AI.")