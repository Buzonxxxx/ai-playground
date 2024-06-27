from dotenv import load_dotenv
from openai import OpenAI
import time
import json

client = OpenAI()

load_dotenv()

# Create assistant
assistant_id = "asst_lBCScAWifdBtQD8i6IR25IAT" # Assistant ID
assistant = client.beta.assistants.retrieve(assistant_id)

# Create thread
thread = client.beta.threads.create()
thread_id = thread.id

# Add message
client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="Louis現在有點焦慮，請安慰一下他！"
)

# Create run
run = client.beta.threads.runs.create(
  thread_id=thread_id,
  assistant_id=assistant.id
)

def poll_run_status(client, thread_id, run_id, interval=2):
    """ 輪詢Run的狀態，直到它不再是'requires_action'或直到完成 """
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run.status in ['requires_action', 'completed']:
            return run
        time.sleep(interval)

run = poll_run_status(client, thread_id, run.id)
print('這時Run讀取了function JSON Schema，然後進入了requires_action狀態\n')
print(run)

def get_function_details(run):
  tool_call = run.required_action.submit_tool_outputs.tool_calls[0]
  return tool_call.function.name, tool_call.function.arguments, tool_call.id

function_name, arguments, function_id = get_function_details(run)
print("function_name:", function_name)
print("arguments:", arguments)
print("function_id:", function_id)

run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

def get_encouragement(mood, name=None):
    encouragement_messages = {
        "開心": "看到你這麼陽光真好！保持這份積極！",
        "難過": "記得，每片烏雲背後都有陽光。",
        "壓力大": "深呼吸，慢慢呼出，一切都會好起来的。",
        "疲倦": "你已经很努力了，现在是时候休息一下了。"
    }

    if name:
        message = f"{name}，{encouragement_messages.get(mood, '抬頭挺胸，一切都會變好的。')}\n"
    else:
        message = encouragement_messages.get(mood, '抬頭挺胸，一切都會變好的。\n')
    
    return message



# 定義可用的函数
available_functions = {
    "get_encouragement": get_encouragement
}

function_args = json.loads(arguments)
function_to_call = available_functions[function_name]
encouragement_message = function_to_call(
    name=function_args.get("name"),
    mood=function_args.get("mood")
)
print(encouragement_message)

def submit_tool_outputs(run, thread, function_id, function_response):
    run = client.beta.threads.runs.submit_tool_outputs(
    thread_id=thread.id,
    run_id=run.id,
    tool_outputs=[
      {
        "tool_call_id": function_id,
        "output": str(function_response),
      }
    ]
    ) 
    return run

run = submit_tool_outputs(run,thread,function_id,encouragement_message)
print('這時，Run收到了结果\n')
print(run)

print('這時，Run繼續執行直到完成\n')
run = poll_run_status(client, thread_id, run.id) 
print(run)

messages = client.beta.threads.messages.list(thread_id=thread_id)
print('下面印出最终的Message')
for message in messages.data:
    if message.role == "assistant":
        print(message.content)