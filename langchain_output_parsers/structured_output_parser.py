from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('HUGGINGFACEHUB_ACCESS_TOCKEN')

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="point_1",description="point 1 about the topic."),
    ResponseSchema(name="point_2",description="point 2 about the topic."),
    ResponseSchema(name="point_3",description="point 3 about the topic.")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Write Some information in 3 points on topic - {topic} \n {format_instructions}",
    input_variables=('topic'),
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser

output = chain.invoke({'topic':'agentic AI'})
print(output)