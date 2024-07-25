import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()

def initialize_openai_client():
    """Initialize and return OpenAI client."""
    return OpenAI()

def generate_image(client, prompt, size="1024x1024", quality="standard", n=1):
    """Generate image using DALL-E 3."""
    return client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=size,
        quality=quality,
        n=n
    )

def download_image(url):
    """Download image from given URL."""
    return requests.get(url)

def save_image(image_content, filename):
    """Save image content to a file."""
    with open(filename, 'wb') as file:
        file.write(image_content)
    print(f"Image saved successfully as {filename}")

def main():
    # Load environment variables
    load_environment()
    # Initialize OpenAI client
    client = initialize_openai_client()
    
    # Define the prompt for image generation
    prompt = "6歲的台灣人Levi即將離開美國回到台灣唸書，美國幼稚園老師班幫他辦歡送派對，請畫一張派對海報並配上文案"
    # Generate image using the defined prompt
    response = generate_image(client, prompt)
    
    # Extract the URL of the generated image
    image_url = response.data[0].url
    # Download the image from the URL
    img = download_image(image_url)
    
    # Define the path where the image will be saved
    dalle_img_path = '歡送派對.png'
    # Save the downloaded image to the defined path
    save_image(img.content, dalle_img_path)

if __name__ == "__main__":
    main()
