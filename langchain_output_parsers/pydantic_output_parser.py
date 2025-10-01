# A python code this uses pydantic output parser and generates some details about a mobile phone

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('HUGGINGFACEHUB_ACCESS_TOCKEN')


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm =llm)


class Specs(BaseModel):
    Processor: str
    RAM: str
    Storage: str
    Battery: str
    camera: str

class Mobile(BaseModel):
    Model_Name : str = Field(description="Name of the model.")
    Model_Specs: Specs = Field(description="Detailed Specifications")
    Price : float = Field(description="price of the model in rupees.")

parser = PydanticOutputParser(pydantic_object=Mobile)

template = PromptTemplate(
    template = "Get Some information about the mobile phone model {model_name} \n {format_instructions}",
    input_variables=('model_name'),
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser

output = chain.invoke({'model_name':'samsung s24'})

print(output)