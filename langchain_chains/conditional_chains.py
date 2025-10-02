<<<<<<< HEAD
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnableBranch
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOCKEN")


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

class sentiment(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="classify the sentiment of the feedback.")

parser1 = PydanticOutputParser(pydantic_object=sentiment)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback in positive or negative class.{feedback}\n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={'format_instructions':parser1.get_format_instructions()}
)

parser2 = StrOutputParser()

classifier_Chain = prompt1 | model | parser1

prompt_negative = PromptTemplate(
    template="Write an appropriate reply to this negative feedback. \n {feedback}",
    input_variables=["feedback"]
)

prompt_positive = PromptTemplate(
    template="Write an appropriate reply to this positive feedback. \n {feedback}",
    input_variables=["feedback"]
)


branch = RunnableBranch(
    (lambda x:x.sentiment=="positive", prompt_positive | model | parser2),
    (lambda x:x.sentiment=="negative", prompt_negative | model | parser2),
    RunnableLambda(lambda x:"feedback not found")
)


chain = classifier_Chain | branch

=======
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnableBranch
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOCKEN")


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

class sentiment(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="classify the sentiment of the feedback.")

parser1 = PydanticOutputParser(pydantic_object=sentiment)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback in positive or negative class.{feedback}\n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={'format_instructions':parser1.get_format_instructions()}
)

parser2 = StrOutputParser()

classifier_Chain = prompt1 | model | parser1

prompt_negative = PromptTemplate(
    template="Write an appropriate reply to this negative feedback. \n {feedback}",
    input_variables=["feedback"]
)

prompt_positive = PromptTemplate(
    template="Write an appropriate reply to this positive feedback. \n {feedback}",
    input_variables=["feedback"]
)


branch = RunnableBranch(
    (lambda x:x.sentiment=="positive", prompt_positive | model | parser2),
    (lambda x:x.sentiment=="negative", prompt_negative | model | parser2),
    RunnableLambda(lambda x:"feedback not found")
)


chain = classifier_Chain | branch

>>>>>>> 7179b9d4 (added langchain_text_splitters)
print(chain.invoke({"feedback":"didnt expected that this product will be this much blunder."}))