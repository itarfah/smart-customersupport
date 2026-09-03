# Smart Customer Support RAG System 
 
## Project Overview 
This project is a Smart Customer Support system that combines Retrieval-Augmented Generation (RAG) with Data Quality Validation. 
The system validates customer support documents, creates embeddings, stores them in ChromaDB, and retrieves relevant information based on the user's question.
 The retrieved context is sent to an LLM through OpenRouter to generate the final answer.

## Project Objectives 
- Build a customer support RAG system. 
- Apply data quality checks before indexing documents. 
- Detect invalid, empty, short, unsupported, and duplicate files. 
- Move invalid documents to a quarantine folder. 
- Generate embeddings and store them in ChromaDB. 
- Retrieve relevant information with its source. 
 
## Architecture 
Customer Support Documents -> Data Quality Validation -> Document Loading -> Text Chunking -> Embeddings -> ChromaDB -> Semantic Retrieval -> LLM Generation -> Answer + Source
 
## Data Quality 
The system checks file type, empty files, minimum content length, and duplicate files before indexing. 
Invalid documents are moved automatically to the data/quarantine folder. 
 
## Technologies Used 
- Python 
- ChromaDB 
- Sentence Transformers 
- all-MiniLM-L6-v2 embedding model 
- PyPDF 
- SHA-256 hashing for duplicate detection
- OpenRouter
- OpenAi python SDK
 
## How to Run 
Install the required packages: 
pip install -r requirements.txt 
 
Run the Data Quality pipeline: 
python app/quality_pipeline.py 
 
Run the Customer Support system: 
python app/main.py 
 
Example question: How long do I have to return a product? 
 
## OpenRouter Setup
This project uses OpenRouter for LLM generation.
Create a .env file in the project root and add your OpenRouter API key:rnrnOPENROUTER_API_KEY=YOUR_API_KEY_HERE
The .env file is ignored by Git and should not be uploaded to GitHub.

## Course 
This project was made for "Modern Data Engineering for AI Systems" course provided by SDAIA Academy. 
https://github.com/SDAIAAcademy
 
## Author 
Tarfah Ahmad Alamer
