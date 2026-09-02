from pathlib import Path

from data_quality import validate_file
from document_loader import load_document, chunk_text
from embedding_model import EmbeddingModel
from vector_store import VectorStore


class RAGPipeline:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def index_knowledge_base(self, knowledge_base_path="data/knowledge_base"):
        knowledge_base = Path(knowledge_base_path)
        known_hashes = set()

        documents = []
        metadatas = []
        ids = []

        for file_path in knowledge_base.iterdir():
            if not file_path.is_file():
                continue

            is_valid, errors, file_hash = validate_file(
                file_path,
                known_hashes
            )

            if not is_valid:
                print(f"Skipped: {file_path.name}")
                print("Errors:", errors)
                continue

            known_hashes.add(file_hash)

            text = load_document(file_path)
            chunks = chunk_text(text)

            for index, chunk in enumerate(chunks):
                documents.append(chunk)

                metadatas.append(
                    {
                        "source": file_path.name
                    }
                )

                ids.append(
                    f"{file_path.stem}_{index}"
                )

        if not documents:
            print("No valid documents found.")
            return

        embeddings = self.embedding_model.embed_documents(documents)

        self.vector_store.add_documents(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        print(f"Indexed {len(documents)} chunks successfully.")

    def retrieve(self, question, n_results=3):
        query_embedding = self.embedding_model.embed_text(question)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            n_results=n_results
        )

        return results
