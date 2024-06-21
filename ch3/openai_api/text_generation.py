from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

print(openai_api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "你是一個幫助使用者了解鮮花訊息的智能助手，並能夠輸出JSON格式的內容"},
        {"role": "user", "content": "生日送什麼花最好?"},
        {"role": "assistant", "content": "玫瑰花是生日禮物的熱門選擇"},
        {"role":"user", "content": "送貨需要多長時間?"}
    ]
)

print(response.choices[0].message.content)

