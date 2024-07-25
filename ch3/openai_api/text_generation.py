from dotenv import load_dotenv
from openai import OpenAI

def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()

def initialize_openai_client():
    """Initialize and return OpenAI client."""
    return OpenAI()

def generate_text(client, messages, model="gpt-3.5-turbo", response_format={"type": "json_object"}):
    """Generate text using OpenAI's chat completions."""
    response = client.chat.completions.create(
        model=model,
        response_format=response_format,
        messages=messages
    )
    return response.choices[0].message.content

def main():
    load_environment()
    client = initialize_openai_client()
    
    messages = [
        {"role": "system", "content": "你是一個幫助使用者了解鮮花訊息的智能助手，並能夠輸出JSON格式的內容"},
        {"role": "user", "content": "生日送什麼花最好?"},
        {"role": "assistant", "content": "玫瑰花是生日禮物的熱門選擇"},
        {"role": "user", "content": "送貨需要多長時間?"}
    ]
    
    response_content = generate_text(client, messages)
    print(response_content)

if __name__ == "__main__":
    main()
