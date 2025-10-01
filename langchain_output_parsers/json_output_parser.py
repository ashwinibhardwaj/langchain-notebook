from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
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

parser = JsonOutputParser()

template = PromptTemplate(
    template = "Write detailed information about mobile phone model \n {model} {format_instructions} ",
    input_variables=(['model']),
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"model":"samsung s24"})

print(result)