import os

API_HOST: str = os.getenv("API_HOST", "127.0.0.1")
API_PORT: int = int(os.getenv("API_PORT", 8080))
API_PATH: str = os.getenv("API_PATH", "").rstrip("/")
