from rag_pipeline import RAGPipeline


def main():
    rag = RAGPipeline()
    print("Preparing knowledge base...")
    rag.index_knowledge_base()

    print("\nSmart Customer Support System")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nAsk a question: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        results = rag.retrieve(question, n_results=1)
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        if not documents:
            print("No answer found.")
            continue

        print("\nAnswer:")
        print(documents[0])
        print("\nSource:")
        print(metadatas[0].get("source", "Unknown") if metadatas else "Unknown")


if __name__ == "__main__":
    main()
