from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

thread_id = 'thread_s2WMFjw73xm0iGy6IphlBzeM'
run_id = 'run_hdGZdzBq8ASh6JgRRw9i1T9d'

polling_interval = 5

import time

while True:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )

    status = run.status
    print(f'Run Status: {status}')

    if status in ['completed', 'failed', 'expired']:
        break

    time.sleep(polling_interval)

if status == 'completed':
    print("Run completed successfully.")
elif status == 'failed' or status == 'expired':
    print("Run failed or expired")