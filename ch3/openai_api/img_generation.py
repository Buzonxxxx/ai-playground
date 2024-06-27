from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="6歲的台灣人Levi即將離開美國回到台灣唸書，美國幼稚園老師班幫他辦歡送派對，請畫一張派對海報並配上文案",
    size="1024x1024",
    quality="standard",
    n=1
    
)

image_url = response.data[0].url
img = requests.get(image_url)

# 將圖片存到本地
dalle_img_path = '歡送派對.png'
with open(dalle_img_path,'wb') as file:
  file.write(img.content)

