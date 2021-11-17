from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(".")/".env"
load_dotenv(dotenv_path=env_path)

class Settings():
	POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
	POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
	POSTGRES_PORT = os.getenv("POSTGRES_PORT") 
	POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
	POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
	POSTGRES_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
	

settings = Settings()
