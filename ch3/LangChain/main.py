from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

prompt = PromptTemplate.from_template("請介紹{flower}是什麼花?")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

output_parser = StrOutputParser()

# Combine prompt, model, and parser into a chain
chain = prompt | llm | output_parser

# Invoke the chain with a sample input
result = chain.invoke({"flower": "玫瑰"})

print(result)
