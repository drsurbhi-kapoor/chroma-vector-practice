import chromadb

client = chromadb.PersistentClient(path= "./chromadb")

collection = client.get_or_create_collection(name = "sample")

print(collection.count())

collection.update(
    ids = ["id0"],
    documents= ["chromadb is a vector database. it sores the embeddings of the etxt and retreive the most similar text"],
    metadatas = [{"topic": "chromadb", "source": "abc.txt"}]
    
)
collection.add(["id1", "id2"],
documents = ["Photosynthesis is how plants make food using sunlight and CO2.",
        "Python is a programming language used for AI and web apps."],
metadatas = [{"topic": "biology", "source": "biology.txt"},
             {"topic":"programming", "source": "python.txt"}]

)
print("total docs: " , collection.count())


result = collection.get(ids = ["id0"],
include = ["metadatas"]
)
print(result["metadatas"])

response = collection.query(
    query_texts = ["How do plants make food?"],
    n_results = 2,
    where_document = {"$contains": "Photosynthesis"}
)
print(response)

collection.delete(ids = ["id2"])
print(collection.count())
