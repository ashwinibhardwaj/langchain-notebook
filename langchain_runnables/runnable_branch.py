<<<<<<< HEAD
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableBranch, RunnablePassthrough
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
    template="Generate a detailed varified news content on the following topic. \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize this content  \n{content}",
    input_variables=["content"]
)

parser = StrOutputParser()


content_generator = RunnableSequence(Prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>=300, prompt2 | model | parser),
    RunnablePassthrough()
)


final_chain = content_generator | branch_chain
output = final_chain.invoke({"topic":"India vs Pakistan Asia Cup 2025 final match winning moments"})

print(output)

=======
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableBranch, RunnablePassthrough
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
    template="Generate a detailed varified news content on the following topic. \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize this content  \n{content}",
    input_variables=["content"]
)

parser = StrOutputParser()


content_generator = RunnableSequence(Prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>=300, prompt2 | model | parser),
    RunnablePassthrough()
)


final_chain = content_generator | branch_chain
output = final_chain.invoke({"topic":"India vs Pakistan Asia Cup 2025 final match winning moments"})

print(output)

>>>>>>> 7179b9d4 (added langchain_text_splitters)
final_chain.get_graph().print_ascii()