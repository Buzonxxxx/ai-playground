# LangChain OpenAI Integration

This project demonstrates the use of LangChain with OpenAI's GPT-3.5-turbo model.

## Prerequisites

- Python 3.6+
- OpenAI API key

## Setup

1. Install dependencies:
   ```sh
   pip install python-dotenv langchain langchain_openai
   ```

2. Create a `.env` file:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

3. Run the script:
   ```sh
   python3 main.py
   ```

## Project Structure

- `main.py`: Contains the main script with functions:
  - `setup_environment()`: Loads environment variables
  - `create_chain()`: Sets up the LangChain processing chain
  - `main()`: Executes the chain with a sample input

## Components

- Environment variables: Managed with `python-dotenv`
- LangChain:
  - `PromptTemplate`: Defines the input prompt
  - `ChatOpenAI`: Initializes the OpenAI model
  - `StrOutputParser`: Parses the model output

The chain combines these components and is invoked with a sample input to generate a response.