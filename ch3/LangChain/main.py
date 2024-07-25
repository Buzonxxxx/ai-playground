from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

def setup_environment():
    """Load environment variables from .env file."""
    load_dotenv()

def create_chain():
    """Create and return a LangChain processing chain."""
    # Define a prompt template for flower introductions
    prompt = PromptTemplate.from_template("請介紹{flower}是什麼花?")
    
    # Initialize the language model
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)
    
    # Set up the output parser
    output_parser = StrOutputParser()
    
    # Combine prompt, language model, and output parser into a chain
    return prompt | llm | output_parser

def main():
    """Main function to run the LangChain flower introduction process."""
    # Set up the environment
    setup_environment()
    
    # Create the processing chain
    chain = create_chain()
    
    # Invoke the chain with a specific flower (rose)
    result = chain.invoke({"flower": "玫瑰"})
    
    # Print the result
    print(result)

if __name__ == "__main__":
    # Execute the main function if this script is run directly
    main()