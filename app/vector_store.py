import chromadb
class VectorStore:
    def __init__(self, db_path="chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name="support_knowledge"
    )

    def add_documents(self, documents, embeddings, metadatas, ids):
        self.collection.upsert(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
    )

    def search(self, query_embedding, n_results=3):
        results = self.collection.query(
             query_embeddings=[query_embedding],
             n_results=n_results
    )

        return results
  