import os

class Config:
    API_KEY = os.getenv("V0_API_KEY", "default_api_key")
    BASE_URL = "https://v0.dev/api"
