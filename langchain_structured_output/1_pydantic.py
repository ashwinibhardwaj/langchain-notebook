from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Load the model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Define schema as a Pydantic model
class Review(BaseModel):
    summary: str
    sentiment: str

# Create structured model
structured_model = model.with_structured_output(Review)

# Invoke
result = structured_model.invoke("the product is not very good")

print(result)
print(result.summary)
print(result.sentiment)
