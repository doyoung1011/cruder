import os
from dotenv import load_dotenv

load_dotenv()

ELASTIC_ENDPOINT = os.getenv('ELASTIC_ENDPOINT')
ELASTIC_API_KEY = os.getenv('ELASTIC_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
ALIO_API_KEY = os.getenv('ALIO_API_KEY')



# MariaDB 접속 정보
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")