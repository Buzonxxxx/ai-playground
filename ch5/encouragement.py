from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()

assistant_id = "asst_lBCScAWifdBtQD8i6IR25IAT" # Agent ID
assistant = client.beta.assistants.retrieve(assistant_id)
print(assistant)

thread = client.beta.threads.create()
print(thread)
thread_id = thread.id

message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="來安慰一下心情低落的Louis！"
)
print(message)

# 运行Assistant来处理Thread
run = client.beta.threads.runs.create(
  thread_id=thread_id,
  assistant_id=assistant.id
)
print(run)

import time
def poll_run_status(client, thread_id, run_id, interval=2):
    """ 輪詢Run的狀態，直到它不再是'requires_action'或直到完成 """
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, 
                                                       run_id=run_id)
        print(run)
        if run.status in ['requires_action', 'completed']:
            return run
        time.sleep(interval)

print('這時，Run應該是進入了requires_action狀態')
run = poll_run_status(client, thread_id, run.id)
print(run)

def get_function_details(run):

  print("\nrun.required_action\n",run.required_action)

  function_name = run.required_action.submit_tool_outputs.tool_calls[0].function.name
  arguments = run.required_action.submit_tool_outputs.tool_calls[0].function.arguments
  function_id = run.required_action.submit_tool_outputs.tool_calls[0].id

  return function_name, arguments, function_id

function_name, arguments, function_id = get_function_details(run)
print("function_name:", function_name)
print("arguments:", arguments)
print("function_id:", function_id)

run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)
print("讀取function JSON 數據之後Run的狀態",run)

def get_encouragement(mood, name=None):
    encouragement_messages = {
        "開心": "看到你这么阳光真好！保持这份积极！",
        "難過": "記得，每片烏雲背後都有陽光。",
        "壓力大": "深呼吸，慢慢呼出，一切都会好起来的。",
        "疲倦": "你已经很努力了，现在是时候休息一下了。"
    }

    # 如果提供了名字，个性化消息
    if name:
        message = f"{name}，{encouragement_messages.get(mood, '抬头挺胸，一切都会变好的。')}"
    else:
        message = encouragement_messages.get(mood, '抬头挺胸，一切都会变好的。')

    return message

import json

# 定义可用的函数字典
available_functions = {
    "get_encouragement": get_encouragement
}

# 解析参数
function_args = json.loads(arguments)

# 动态调用函数
function_to_call = available_functions[function_name]
encouragement_message = function_to_call(
    name=function_args.get("name"),
    mood=function_args.get("mood")
)

# 打印结果以进行验证
print(encouragement_message)