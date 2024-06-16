from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import os
import time

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# Read file
file_path = 'sales_data.csv'
sales_data = pd.read_csv(file_path)

# Create doc
file = client.files.create(
    file=open(file_path, 'rb'),  # read binary
    purpose='assistants'
)
# Create agent with doc
assistant = client.beta.assistants.create(
    name="數據分析師",
    instructions="作為一位數據科學助理，當給定數據和一個查詢時，你能編寫適當的程式碼並創建適當的視覺化。",
    model="gpt-4o",
    tools=[{ "type": "code_interpreter" }],
    tool_resources={
        "code_interpreter": {
            "file_ids": [file.id]
        }
    }
)
print(assistant)
print("----------")

# Create thread
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "計算從2022年到2025年每個季度的總銷售總額，並通過不同的產品將其可視化為折線圖，產品線條顏色分別為紅，藍，綠。",
            "attachments": [
                {
                    "file_id": file.id,
                    "tools": [
                        {"type": "code_interpreter"}
                    ]
                }
            ]
        }
    ]
)
print(thread)
print("----------")

# Create run
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
print(run)
print("----------")

# Wait run to finish
while True:
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    try:
        messages.data[0].content[0].image_file
        time.sleep(5)
        print("圖表已建立")
        if messages.data and messages.data[0].content:
            print("當前Message: ", messages.data[0].content[0])
        break
    except:
        time.sleep(10)
        print("你的助手正在努力的做圖表....")
        if messages.data and messages.data[0].content:
            print("當前Message: ", messages.data[0].content[0])

# Convert output file to png sand save it
def convert_file_to_png(file_id, write_path):
    data = client.files.content(file_id)
    data_bytes = data.read()
    with open(write_path, "wb") as file:
        file.write(data_bytes)

plot_file_id = messages.data[0].content[0].image_file.file_id
image_path = "圖書銷售.png"
convert_file_to_png(plot_file_id, image_path)

# Upload png file
plot_file = client.files.create(
  file=open(image_path, "rb"),
  purpose='assistants'
)

# messages = client.beta.threads.messages.list(thread_id=thread.id)
# [message.content[0] for message in messages.data]

# Define submit message function
def submit_message_wait_completion(assistant_id, thread, user_message, file_ids=None):
    for run in client.beta.threads.runs.list(thread_id=thread.id).data:
        if run.status == 'in_progress':
            print(f"等待Run {run.id} 完成...")
            while True:
                run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id).status
                if run_status in ['succeeded', 'failed']:
                    break
                time.sleep(5)  # wait for 5s then check again

    params = {
        'thread_id': thread.id,
        'role': 'user',
        'content': user_message,
    }
    if file_ids:        
        attachments = [{"file_id": file_id, "tools": [ {"type": "code_interpreter"}]} for file_id in file_ids]
        params['attachments'] = attachments
    client.beta.threads.messages.create(**params)

    # 创建Run
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)
    return run 


def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id)

submit_message_wait_completion(assistant.id, thread, "請根據你剛才建立的圖表，给我兩個约20字的句子，描述最重要的洞察。這會用來做投影片展示，揭露出數據背後的'秘密'。")
time.sleep(10)
response = get_response(thread)
bullet_points = response.data[0].content[0].text.value
print(bullet_points)
print("----------")

submit_message_wait_completion(assistant.id, thread, "根據你創建的情節和要點，為投影片想一個非常簡短的標題。它應該只反映你得出的主要見解。")
time.sleep(10)
response = get_response(thread)
title = response.data[0].content[0].text.value
print(title)
print("----------")