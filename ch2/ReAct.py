from dotenv import load_dotenv
load_dotenv()  

# 從hub中獲取React的Prompt
from langchain import hub
prompt = hub.pull("hwchase17/react")
print(prompt)

from langchain_openai import OpenAI
llm = OpenAI()

from langchain_community.utilities import SerpAPIWrapper
from langchain.agents.tools import Tool
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="當大模型沒有相關知識時，用於搜索知識"
    ),
]

from langchain.agents import create_react_agent
agent = create_react_agent(llm, tools, prompt)

from langchain.agents import AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print("第一次運行的结果：")
agent_executor.invoke({"input": "當前Agent最新研究進展是什麼?"})
print("第二次運行的结果：")
agent_executor.invoke({"input": "當前Agent最新研究進展是什麼?"})