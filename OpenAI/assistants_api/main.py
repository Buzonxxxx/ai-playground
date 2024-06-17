from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# Create assistant
assistant = client.beta.assistants.create(
    name="幼兒籃球教練",
    instructions="你是一位國小籃球專任教練，擅長針對12歲以下小孩的籃球訓練",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo",
)

# Create thread
thread = client.beta.threads.create()

# Add message
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="一位九歲的小男孩，應該從哪些方面加強籃球技能"
)

# Create run
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id
)

if run.status == 'completed': 
  messages = client.beta.threads.messages.list(thread_id=thread.id)
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
else:
  print(run.status)
