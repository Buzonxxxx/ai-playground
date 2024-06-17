from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

assistants = client.beta.assistants.list()

if hasattr(assistants, 'data'):
    files = assistants.data
else:
    print("No data attribute in the response.")
    files = []

print(assistants)

for assistant in assistants:
    assistant_id = assistant.id
    try:
        client.beta.assistants.delete(assistant_id)
        print(f"Deleted file: {assistant_id}")
    except Exception as e:
        print(f"Failed to delete file: {assistant_id}. Error: {e}")
print("All assistants processed.")
