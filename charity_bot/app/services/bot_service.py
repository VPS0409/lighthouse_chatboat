from sentence_transformers import SentenceTransformer
import torch
import pickle
import base64
from app.database import crud
from app.config import Config

class CharityBotService:
    def __init__(self):
        self.model = SentenceTransformer(Config.EMBEDDING_MODEL)
        
    async def find_best_answer(self, question: str) -> str:
        # Получаем все эмбеддинги из БД
        examples = await crud.get_all_examples()
        
        # Сравниваем с вопросом пользователя
        question_embedding = self.model.encode(question)
        best_match = None
        best_score = 0.0
        
        for example in examples:
            embedding = pickle.loads(base64.b64decode(example.embedding))
            score = util.pytorch_cos_sim(
                torch.tensor(question_embedding),
                torch.tensor(embedding)
            ).item()
            
            if score > best_score:
                best_score = score
                best_match = example
        
        return best_match.intent.answer.answer_text if best_score > 0.7 else None