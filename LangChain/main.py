from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt template
prompt = PromptTemplate.from_template("{flower}是誰?")

# Initialize the ChatOpenAI model with a supported model name
model = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo", temperature=0.1)

# Initialize the output parser
output_parser = StrOutputParser()

# Combine prompt, model, and parser into a chain
chain = prompt | model | output_parser

# Invoke the chain with a sample input
result = chain.invoke({"flower": "百合"})

# Print the result
print(result)
