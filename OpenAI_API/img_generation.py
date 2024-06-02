import os

api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

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

