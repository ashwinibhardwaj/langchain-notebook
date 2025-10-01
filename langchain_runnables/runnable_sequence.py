from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOCKEN")

llm = HuggingFaceEndpoint(
    model="openai/gpt-oss-120b",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm = llm)
Prompt1 = PromptTemplate(
    template="Generate a joke on the topic {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain me this joke in short \n{joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()


chain = RunnableSequence(Prompt1, model, parser, prompt2, model, parser)

output = chain.invoke({"topic":"Dog"})

print(output)

chain.get_graph().print_ascii()