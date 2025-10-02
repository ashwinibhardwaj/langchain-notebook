<<<<<<< HEAD
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke("What is the capital of india.")
=======
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke("What is the capital of india.")
>>>>>>> 7179b9d4 (added langchain_text_splitters)
print(result)