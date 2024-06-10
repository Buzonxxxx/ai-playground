from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# Create assistant
assistant = client.beta.assistants.create(
    name="幼兒籃球教練",
    instructions="幫我訓練9歲小孩的籃球技能",
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
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="請回答問題"
)

print(run)