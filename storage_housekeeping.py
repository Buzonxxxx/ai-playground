from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

files = client.files.list()

if hasattr(files, 'data'):
    files = files.data
else:
    print("No data attribute in the response.")
    files = []

print(files)

for file in files:
    file_id = file.id
    try:
        client.files.delete(file_id)
        print(f"Deleted file: {file_id}")
    except Exception as e:
        print(f"Failed to delete file: {file_id}. Error: {e}")
print("All files deleted.")
