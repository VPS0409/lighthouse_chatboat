# app/services/bot_service.py
from sentence_transformers import SentenceTransformer
from app.database import crud
from app.config import Config

class CharityBot:
    def __init__(self):
        self.model = SentenceTransformer(Config.EMBEDDING_MODEL)
        
    def add_complete_question(self, main_question: str, answer_text: str, variations: list):
        """Полный цикл добавления вопроса (публичный метод)"""
        # Используем функцию из crud.py
        crud.add_new_question(
            intent_name=main_question,
            answer_text=answer_text,
            examples=[main_question] + variations
        )
        
        # Дополнительная обработка эмбеддингов
        self._process_embeddings(main_question, variations)