from rag_pipeline import RAGPipeline

rag = RAGPipeline()
print("Indexing knowledge base...")
rag.index_knowledge_base()

question = "How long do I have to return a product?"
print("\nQuestion:")
print(question)

results = rag.retrieve(question, n_results=3)
print("\nRetrieved results:")
for i, document in enumerate(results["documents"][0], start=1):
    source = results["metadatas"][0][i - 1]["source"]

    print(f"\nResult {i}")
    print("Source:", source)
    print("Text:", document)
