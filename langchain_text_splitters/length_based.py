from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('data/Designing_MachineLearning_Systems.pdf')

doc = loader.load()


splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=10,
    separator=" "
    )


splitted_doc = splitter.split_documents(documents=doc)

print(splitted_doc[0].page_content)

