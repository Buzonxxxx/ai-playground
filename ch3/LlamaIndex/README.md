# LlamaIndex OpenAI Integration

This project demonstrates the use of LlamaIndex with OpenAI's API to create and query a document index.

## Prerequisites

- Python 3.6+
- OpenAI API key

## Setup

1. Install dependencies:
   ```sh
   pip install python-dotenv llama_index
   ```

2. Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

3. Run the script:
   ```sh
   python3 main.py
   ```

## Project Structure

- `main.py`: Contains the main script with functions:
  - `load_environment()`: Loads environment variables
  - `create_index()`: Creates and persists a VectorStoreIndex from documents
  - `query_index()`: Queries the index with a given question
  - `main()`: Demonstrates index creation and querying

## Components

- Environment variables: Managed with `python-dotenv`
- Document reading: Uses `SimpleDirectoryReader` to load documents from the 'data' directory
- Index creation: Utilizes `VectorStoreIndex` to create an index from documents
- Querying: Employs a query engine to execute queries on the index
- Persistence: Saves the index's storage context for future use

The script creates an index from documents, persists it, and then demonstrates querying with a sample question.
