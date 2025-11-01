from chromadb.utils import embedding_functions


# we can use many embedding_functions from different vendors.
func = embedding_functions.DefaultEmbeddingFunction()

name = [ "Paulo" ]

embedding = func(name)

print(embedding)
