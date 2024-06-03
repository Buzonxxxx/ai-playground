from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="電商花語秘境的新春玫瑰花宣傳海報，配上文案",
    size="1024x1024",
    quality="standard",
    n=1
    
)

image_url = response.data[0].url
print(image_url)

