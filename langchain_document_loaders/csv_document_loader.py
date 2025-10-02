from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("data/diabetes.csv")

data = loader.load()

print(data[0].page_content)