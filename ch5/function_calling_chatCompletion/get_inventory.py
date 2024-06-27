from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()  
client = OpenAI()

def get_flower_inventory(city):
    """獲取指定城市的鲜花庫存"""
    if "北京" in city:
        return json.dumps({"city": "北京", "inventory": "玫瑰: 100, 鬱金香: 150"})
    elif "上海" in city:
        return json.dumps({"city": "上海", "inventory": "百合: 80, 康乃馨: 120"})
    elif "深圳" in city:
        return json.dumps({"city": "深圳", "inventory": "向日葵: 200, 玉蘭花: 90"})
    else:
        return json.dumps({"city": city, "inventory": "未知"})

# JSON Schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_flower_inventory",
            "description": "獲取指定城市的鮮花庫存",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名稱，例如：北京、上海或深圳"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# 第一次對話的Message
messages = [{"role": "user", "content": "北京、上海和深圳的鮮花庫存是多少？請用台灣文回答"}]
print("初始消息:", messages)

# 第一次對話的结果
first_response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)
response_message = first_response.choices[0].message
tool_calls = response_message.tool_calls

# 如果結果要求用Function Call，就調用函數，並把函數的查詢结果附加到消息中
if tool_calls:
    messages.append(response_message)
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        function_response = get_flower_inventory(
            city=function_args.get("city")
        )
        messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            }
        )
print("\n更新後的消息:", messages)

# 用有了庫存查詢结果的Message再來一次對話
second_response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=messages
    )
response_content = second_response.choices[0].message.content

print("\n第二次對話結果:")
print(response_content)