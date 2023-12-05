import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    together_api_key = os.getenv("TOGETHER_API_KEY")


cfg = Config()