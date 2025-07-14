# app/services/embedding.py
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingProcessor:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)
    
    def get_embedding(self, text: str) -> np.ndarray:
        return self.model.encode(text)
    
    def save_to_db(self, embedding: np.ndarray):
        # Логика сохранения в БД
        pass