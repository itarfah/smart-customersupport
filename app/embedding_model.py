from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_text(self, text):
        embedding = self.model.encode(text)
        return embedding.tolist()

    def embed_documents(self, documents):
        embeddings = self.model.encode(documents)
        return embeddings.tolist()
