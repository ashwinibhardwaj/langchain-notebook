from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L12-v2")

document = [
"Virat Kohli: Renowned for his aggressive batting style, Virat Kohli is one of India's most successful cricket captains and a modern-day run machine.",
"Rohit Sharma: Known as the 'Hitman' of Indian cricket, Rohit Sharma holds the record for the highest individual score in a One Day International match.",
"MS Dhoni: Celebrated for his calm demeanor and exceptional leadership, MS Dhoni led India to World Cup victories in both T20 and ODI formats.",
"Sachin Tendulkar: Widely regarded as one of the greatest cricketers of all time, Sachin Tendulkar is the highest run-scorer in the history of international cricket.",
"Jasprit Bumrah: Famous for his unique bowling action and deadly yorkers, Jasprit Bumrah is one of India's premier fast bowlers.",
"Hardik Pandya: An explosive all-rounder, Hardik Pandya is known for his big hitting and valuable contributions with both bat and ball."
]

query = "Who is known as hitman"

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]


print(query)
print(document[index])
print(score)



