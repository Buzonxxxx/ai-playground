from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()

# Read documents from the 'data' directory
documents = SimpleDirectoryReader("data").load_data()

# Create an index from the documents, with a fallback to another model
index = VectorStoreIndex.from_documents(documents, model="text-embedding-ada-002")

# Create a query engine from the index
query_engine = index.as_query_engine()

# Execute a query
response = query_engine.query("競賽班一年要打多少比賽?")

print("競賽班一年要打多少比賽?", response)

# Persist the index storage context
index.storage_context.persist()
