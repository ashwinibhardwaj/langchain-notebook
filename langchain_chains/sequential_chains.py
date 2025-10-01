from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOCKEN")

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template = "Write a detailed guide on the topic {topic}",
    input_variables=('topic')
)

prompt2 = PromptTemplate(
    template= "Extract 5 most important key points from this text \n {text} \n write in paragraph and list format and dont include any kind of formatting ",
    input_variables=('text')
)


parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "RAG"})
print(result)