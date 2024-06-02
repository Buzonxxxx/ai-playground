from dotenv import load_dotenv
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load environment variables from .env file
load_dotenv()

# Read documents from the 'data' directory
documents = SimpleDirectoryReader("data").load_data()

# Retrieve the API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Create an index from the documents, with a fallback to another model
index = VectorStoreIndex.from_documents(documents, model="text-embedding-ada-002", api_key=openai_api_key)

# Create a query engine from the index
query_engine = index.as_query_engine()

# Execute a query
response = query_engine.query("總共有幾筆消費?")

# Print the response
print("總共有幾筆消費?", response)

# Persist the index storage context
index.storage_context.persist()
