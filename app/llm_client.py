import os
from dotenv import load_dotenv
from openai import OpenAI


class LLMClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")

        self.model = os.getenv(
            "OPENROUTER_MODEL",
            "openrouter/free"
        )

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )

    def generate_answer(self, question, context):
        prompt = f"""
Answer the customer's question using only the context below. If the answer is not found in the context, say that the information is not available.

Context:
{context}

Question:
{question}
"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
