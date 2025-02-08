import os

_DEFAULT_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "https://pesaventofilippo.github.io"
]

API_HOST: str = os.getenv("API_HOST", "127.0.0.1")
API_PORT: int = int(os.getenv("API_PORT", 8080))
API_PATH: str = os.getenv("API_PATH", "").rstrip("/")
ALLOWED_ORIGINS: list[str] = os.getenv("ALLOWED_ORIGINS", ",".join(_DEFAULT_ORIGINS)).split(",")
