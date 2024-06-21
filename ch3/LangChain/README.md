# README

## Overview

This script demonstrates how to use the LangChain library to interact with OpenAI's GPT-3.5-turbo model. It loads environment variables from a `.env` file, retrieves the OpenAI API key, and sets up a chain consisting of a prompt template, the OpenAI model, and an output parser. The script then invokes the chain with a sample input to get a response from the model.

## Prerequisites

- Python 3.6 or higher
- `python-dotenv` package
- `langchain` and `langchain_openai` packages
- OpenAI API key

## Setup

1. **Install required packages:**
   ```sh
   pip install python-dotenv langchain langchain_openai
    ```
2. **Create a .env file in the root directory of your project and add your OpenAI API key:**
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```
3. **Run the file**
   ```sh
   python3 main.py
   ```

# Explanation
- **Environment Variables:**

  - The script uses the dotenv package to load environment variables from a `.env` file. This is useful for keeping sensitive information like API keys secure.

- **OpenAI API Key:**
  - The API key is retrieved from the environment variable `OPENAI_API_KEY`.

- **LangChain Components:**

  - **PromptTemplate:** Defines the template for the prompt that will be sent to the OpenAI model.
  - **ChatOpenAI:** Initializes the OpenAI chat model with the specified API key and model parameters.
  - **StrOutputParser:** Parses the output from the model.
- **Chain Invocation:**
  - The chain combines the prompt, model, and output parser. It is invoked with a sample input to get a response from the model.
