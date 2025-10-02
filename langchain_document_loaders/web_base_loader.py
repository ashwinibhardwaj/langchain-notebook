from langchain_community.document_loaders import WebBaseLoader


url = "https://en.wikipedia.org/wiki/LangChain"

loader = WebBaseLoader(web_path=url)
data = loader.load()

print(data[0].page_content)