# README

## Overview

This script demonstrates how to use the OpenAI API to interact with the OpenAI API.

## Prerequisites

- Python 3.6 or higher
- `python-dotenv` and `openai` package
- OpenAI API key

## Setup

1. **Install required packages:**
   ```sh
   pip install python-dotenv openai
   ```
2. **Create a .env file in the root directory of your project and add your OpenAI API key:**
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```
3. **Run the file**
   ```sh
   python3 text_generation.py
   python3 img_generation.py
   ```

## Code
### Text Generation
text_generation.py
```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

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
```

### Image Generation
img_generation.py
```python
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
```