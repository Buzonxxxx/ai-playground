from dotenv import load_dotenv
from langchain import hub
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor

# 加載環境變量
load_dotenv()  

# 從hub中獲取React的Prompt
prompt = hub.pull("hwchase17/react")
print("獲取的Prompt: ", prompt)

# 初始化OpenAI LLM
llm = OpenAI()

# 設置SerpAPI工具
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="當大模型沒有相關知識時，用於搜索知識"
    ),
]

# 創建React代理
agent = create_react_agent(llm, tools, prompt)

# 初始化代理執行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 執行代理並打印結果
def run_agent(input_text):
    print("======")
    print(f"輸入: {input_text}")
    result = agent_executor.invoke({"input": input_text})
    print(f"結果: {result}")
    print("======")
    return result

# 第一次運行
run_agent("當前Agent最新研究進展是什麼?")

# 第二次運行
run_agent("當前Agent最新研究進展是什麼?")
