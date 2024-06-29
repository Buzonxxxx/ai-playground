from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

# Persist the index storage context
index.storage_context.persist()

# Create a query engine from the index
query_engine = index.as_query_engine()

# Execute a query
response = query_engine.query("競賽班一年要打多少比賽?")

print("競賽班一年要打多少比賽?", response)
