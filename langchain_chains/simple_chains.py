from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

prompt = PromptTemplate(
    template= "Tell 5 interesting facts about the topic {topic}",
    input_variables=("topic")
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Langchain'})
print(result)


chain.get_graph().print_ascii()
