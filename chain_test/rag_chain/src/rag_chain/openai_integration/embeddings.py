import openai
from rag_chain.core.config import settings

def get_embeddings(texts):
    response = openai.Embedding.create(
        model="text-similarity-babbage-001",
        input=texts
    )
    return response["data"]

