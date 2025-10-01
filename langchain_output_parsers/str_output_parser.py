from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOCKEN")

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm = llm)

template1 = PromptTemplate(
    template = "Write a detailed guide on the topic {topic}",
    input_variables=(['topic'])
)

template2 = PromptTemplate(
    template = "Write a 5 line summary from the text \n {text}",
    input_variables=(['text'])
)


parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

output = chain.invoke({"topic":"Agentic AI"})
print(output)

