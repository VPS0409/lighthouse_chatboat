import os
from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).parent.parent
    
    # Настройки БД
    DB_USER = os.getenv("DB_USER", "bot_user")
    DB_PASS = os.getenv("DB_PASS", "secure_password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "charity_bot")
    
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    
    # Настройки модели
    EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
    
    # Настройки сервера
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")