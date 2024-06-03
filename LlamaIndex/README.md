# README

## Overview

This script demonstrates how to use the `llama_index` library to interact with OpenAI's API. It reads documents from a specified directory, creates an index from these documents using a specified model, and allows querying the index. The script also persists the index's storage context for future use.

## Prerequisites

- Python 3.6 or higher
- `python-dotenv` package
- `llama_index` package
- OpenAI API key

## Setup

1. **Install required packages:**
   ```sh
   pip install python-dotenv llama_index
   ```
2. **Create a .env file in the root directory of your project and add your OpenAI API key:**
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```
3. **Run the file**
   ```sh
   python3 main.py
   ```

## Explanation

- **Environment Variables**:
  - The script uses the `dotenv` package to load environment variables from a `.env` file. This is useful for keeping sensitive information like API keys secure.

- **Reading Documents**:
  - Documents are read from the 'data' directory using `SimpleDirectoryReader`.

- **Creating an Index**:
  - An index is created from the documents using the `VectorStoreIndex` class with the specified model and API key.

- **Query Engine**:
  - A query engine is created from the index to allow querying.

- **Executing a Query**:
  - The script queries the index with a sample question and prints the response.

- **Persisting the Index**:
  - The index's storage context is persisted for future use.
