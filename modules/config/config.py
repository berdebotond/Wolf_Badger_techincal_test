"""
Config module.
"""
import dataclasses
import os
import uuid
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


@dataclasses.dataclass
class Config:
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", True)
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", 5000))
    GITHUB_CLIENT_ID: str = os.getenv("GITHUB_CLIENT_ID", "")
    GITHUB_CLIENT_SECRET: str = os.getenv("GITHUB_CLIENT_SECRET", "")
    GITHUB_REDIRECT_URI: str = os.getenv("GITHUB_REDIRECT_URI", "http://localhost:5000/github/callback")
    GITHUB_API_BASEURL: str = "https://api.github.com"
    # generate a UUID for the secret key
    APP_SECRET_KEY: str = os.getenv("API_SECRET_KEY", str(uuid.uuid4()))
    # from compose file  for prostiqsql
    DB_URI: str = os.getenv("DB_URI", 'postgresql://postgres:example@localhost:5432/postgres')


cfg = Config()
if not cfg.GITHUB_CLIENT_ID or not cfg.GITHUB_CLIENT_SECRET:
    raise ValueError("GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET is not set, please create a .env file or add them to "
                     "the environment variables.")
