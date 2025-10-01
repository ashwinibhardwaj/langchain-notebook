from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOCKEN")


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=api_key
)


model = ChatHuggingFace(llm=llm)


template1 = PromptTemplate(
    template="Write a detailed guide on topic {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Write a 5 line summary from this text. \n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({"topic":"Agentic AI"})

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text":result.content})

result1 = model.invoke(prompt2)

print(result1.content)