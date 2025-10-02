<<<<<<< HEAD
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L12-v2"
)

text = "i am ashwini"

result = embedding.embed_query(text)

print(str(result))
=======
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L12-v2"
)

text = "i am ashwini"

result = embedding.embed_query(text)

print(str(result))
>>>>>>> 7179b9d4 (added langchain_text_splitters)
