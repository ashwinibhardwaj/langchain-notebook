from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


st.header("Research Tool")


paper_input = st.selectbox("Select a Research paper Name:",['Select...','Attenton is all you need','Bert:pre-training of deep bidirectional transformers','Gpt-3 lamguage models are few shot leners'])

style_input = st.selectbox("Select Explaination Style",['Beginer-Friendly','Technical''code oriented','mathematical'])

length_input = st.selectbox('Select Explanation length',['Short(1-2 paragraphs)','Medium(3-5 paragraphs)','long(Detailed explanation)'])


template = load_prompt("template.json")

prompt = template.invoke({
    "paper_input" : paper_input,
    "style_input" : style_input,
    "length_input" : length_input
})


if st.button('Enter'):
    result = model.invoke(prompt)
    st.write(result.content)