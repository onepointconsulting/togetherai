import os
from dotenv import load_dotenv
from openai import AsyncOpenAI


load_dotenv()


class Config:
    together_api_key = os.getenv("TOGETHER_API_KEY")
    together_model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    temperature = 0.0
    # Initialize the OpenAI client
    open_ai_client = AsyncOpenAI(
        api_key=together_api_key, 
        base_url="https://api.together.xyz/v1",
        timeout=30
    )


cfg = Config()
