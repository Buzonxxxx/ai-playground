# OpenAI API Integration

This project demonstrates how to interact with the OpenAI API for text generation and image creation.

## Prerequisites

- Python 3.6+
- OpenAI API key
- Required Python packages: `python-dotenv`, `openai`, `requests`

## Setup

1. Install required packages:
   ```sh
   pip install python-dotenv openai requests
   ```

2. Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

3. Run the scripts:
   ```sh
   python3 text_generation.py
   python3 img_generation.py
   ```

## Project Structure

### Text Generation (`text_generation.py`)

This script demonstrates how to use OpenAI's API for text generation:

- Loads environment variables
- Initializes the OpenAI client
- Generates text using chat completions
- Outputs the response in JSON format

Key functions:
- `load_environment()`: Loads environment variables
- `initialize_openai_client()`: Initializes the OpenAI client
- `generate_text()`: Generates text using OpenAI's chat completions

### Image Generation (`img_generation.py`)

This script shows how to use OpenAI's DALL-E 3 for image generation:

- Loads environment variables
- Initializes the OpenAI client
- Generates an image based on a prompt
- Downloads and saves the generated image

Key functions:
- `load_environment()`: Loads environment variables
- `initialize_openai_client()`: Initializes the OpenAI client
- `generate_image()`: Generates an image using DALL-E 3
- `download_image()`: Downloads the generated image
- `save_image()`: Saves the image to a file

## Usage

Both scripts can be run independently to demonstrate their respective functionalities. Modify the prompts or parameters in the `main()` function of each script to experiment with different inputs and outputs.