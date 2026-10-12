import chromadb
from chromadb.utils.data_loaders import ImageLoader
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction

client = chromadb.PersistentClient(path = "./chromadb_multimodal")

collection = client.get_or_create_collection(
    name = "image_search",
    embedding_function= OpenCLIPEmbeddingFunction(),
    data_loader = ImageLoader(),
)
if collection.count() == 0: 
    collection.add(
        ids = ["cat", "nature"],
        uris= [
            "./images/cat_1_renamed.jpg",
            "./images/nature_1.jfif"
        ],
    metadatas = [
        {"type": "animal", "label": "cat"},
        {"type": "nature", "label": "nature"}
        
    ]
    )

collection.update(ids = ["cat"],
uris = ["./images/cat_1_renamed.jpg"]

)

result_1= collection.get(
    ids = ["cat"],
    include = ["metadatas", "uris"]
)
print(result_1)

results = collection.query(
    query_texts=["show the picture of cats"],
    n_results=2,
    include=["uris", "distances"]
)

print(results)
