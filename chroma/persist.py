import chromadb
from chromadb.utils import embedding_functions

func = embedding_functions.DefaultEmbeddingFunction()

client = chromadb.PersistentClient("./db/persist")

collection = client.
