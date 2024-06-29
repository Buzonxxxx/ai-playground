from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor

load_dotenv()

llm = ChatOpenAI(model='gpt-4-turbo-preview', temperature=0.5)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

template = ('''
    '盡你所能用中文回答以下問題。如果能力不夠你可以使用以下工具:\n\n'
    '{tools}\n\n
    Use the following format:\n\n'
    'Question: the input question you must answer\n'
    'Thought: you should always think about what to do\n'
    'Action: the action to take, should be one of [{tool_names}]\n'
    'Action Input: the input to the action\n'
    'Observation: the result of the action\n'
    '... (this Thought/Action/Action Input/Observation can repeat N times)\n'
    'Thought: I now know the final answer\n'
    'Final Answer: the final answer to the original input question\n\n'
    'Begin!\n\n'
    'Question: {input}\n'
    'Thought:{agent_scratchpad}' 
    '''
)
prompt = PromptTemplate.from_template(template)

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, 
                               tools=tools, 
                               handle_parsing_errors=True,
                               verbose=True)

agent_executor.invoke({"input": 
                       """目前在台灣市場上玫瑰花的一般進貨價格是多少台幣？\n
                       如果我在此基礎上上加價5%，應該如何定價？"""})