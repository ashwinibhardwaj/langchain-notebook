# a simple application to demonstrate runnable_parallel - to model generates two different jokes about a given topic parallaly and a final model ranks the jokes based on content quality.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOCKEN")
 
llm1 = HuggingFaceEndpoint(
    model="openai/gpt-oss-120b",
    huggingfacehub_api_token=api_key
)

llm2 = HuggingFaceEndpoint(
    model="openai/gpt-oss-20b",
    huggingfacehub_api_token=api_key
)

llm3 = HuggingFaceEndpoint(
    model = "meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token= api_key
)
model1 = ChatHuggingFace(llm = llm1)

model2 = ChatHuggingFace(llm = llm2)

model3 = ChatHuggingFace(llm = llm3)



prompt1 = PromptTemplate(
    template = "Generate a joke in hinglish on the topic - {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Rank these jokes based on the content quality and humar.\n {joke1}, {joke2}",
    input_variables=['joke1','joke2']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "joke1" : RunnableSequence(prompt1, model1, parser),
    "joke2" : RunnableSequence(prompt1, model2, parser )
})
merge_chain = RunnableSequence(prompt2, model3, parser)

final_chain = RunnableSequence(parallel_chain, merge_chain)

output = final_chain.invoke({'topic':'Donkey'})

print(output)

final_chain.get_graph().print_ascii()
