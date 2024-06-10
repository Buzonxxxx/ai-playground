from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

thread_id = 'thread_s2WMFjw73xm0iGy6IphlBzeM'

messages = client.beta.threads.messages.list(
    thread_id=thread_id
)

# print(messages)
# Extract and format the messages
for message in messages.data:
    print(f"Message ID: {message.id}")
    print(f"Role: {message.role}")
    print(f"Assistant ID: {message.assistant_id}")
    print(f"Created At: {message.created_at}")
    print("Content:")
    for content_block in message.content:
        if content_block.type == 'text':
            print(content_block.text.value)
    print("\n")