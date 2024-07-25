# Import required libraries
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()

def create_index():
    """Create and persist a VectorStoreIndex from documents in the 'data' directory."""
    # Load documents from the 'data' directory
    documents = SimpleDirectoryReader("data").load_data()
    # Create an index from the documents
    index = VectorStoreIndex.from_documents(documents)
    # Persist the index's storage context
    index.storage_context.persist()
    return index

def query_index(index, question):
    """Query the index with a given question."""
    # Create a query engine from the index
    query_engine = index.as_query_engine()
    # Execute the query and return the response
    return query_engine.query(question)

def main():
    """Main function to demonstrate index creation and querying."""
    # Load environment variables
    load_environment()
    # Create the index
    index = create_index()
    # Define a sample question
    question = "競賽班一年要打多少比賽?"
    # Query the index and get the response
    response = query_index(index, question)
    # Print the question and response
    print(f"{question} {response}")

if __name__ == "__main__":
    main()
