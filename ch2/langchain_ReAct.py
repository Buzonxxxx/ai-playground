# Import necessary libraries
from dotenv import load_dotenv
from langchain import hub
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor

def load_environment():
    # Load environment variables
    load_dotenv()

def get_react_prompt():
    # Get ReAct prompt from Langchain Hub
    prompt = hub.pull("hwchase17/react")
    print("Retrieved Prompt: ", prompt)
    return prompt

def initialize_llm():
    # Initialize OpenAI language model
    return OpenAI()

def setup_tools():
    # Set up search tool
    search = SerpAPIWrapper()
    return [
        Tool(
            name="Search",
            func=search.run,
            description="Used for searching knowledge when the large model lacks relevant information"
        ),
    ]

def create_agent(llm, tools, prompt):
    # Create ReAct agent
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)

def run_agent(agent_executor, input_text):
    # Run agent and print results
    print("======")
    print(f"Input: {input_text}")
    result = agent_executor.invoke({"input": input_text})
    print(f"Result: {result}")
    print("======")
    return result

def main():
    # Main function: set up environment, create agent, and run
    load_environment()
    prompt = get_react_prompt()
    llm = initialize_llm()
    tools = setup_tools()
    agent_executor = create_agent(llm, tools, prompt)

    # Run twice
    for _ in range(2):
        run_agent(agent_executor, "What are the latest research developments in the current Agent?")

if __name__ == "__main__":
    main()
