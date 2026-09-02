from rag_pipeline import RAGPipeline
from llm_client import LLMClient


def main():
    rag = RAGPipeline()
    llm = LLMClient()
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

        results = rag.retrieve(question, n_results=3)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        if not documents:
            print("No answer found.")
            continue

        context = "\n\n".join(documents)

        answer = llm.generate_answer(
            question=question,
            context=context
        )

        sources = []

        for metadata in metadatas:
            source = metadata["source"]

            if source not in sources:
                sources.append(source)

        print("\nAnswer:")
        print(answer)

        print("\nSources:")

        for source in sources:
            print("-", source)


if __name__ == "__main__":
    main()
