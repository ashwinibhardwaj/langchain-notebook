from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('data/Ashwini_Bhardwaj_Resume.pdf')

data = loader.load()

print(data[0].page_content)