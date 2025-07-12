from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from app.database.session import Base

class Answer(Base):
    __tablename__ = "answers"
    
    answer_id = Column(Integer, primary_key=True)
    answer_text = Column(Text, nullable=False)

class Intent(Base):
    __tablename__ = "intents"
    
    intent_id = Column(Integer, primary_key=True)
    intent_name = Column(String(255), nullable=False)
    answer_id = Column(Integer, ForeignKey("answers.answer_id"))

class IntentExample(Base):
    __tablename__ = "intent_examples"
    
    example_id = Column(Integer, primary_key=True)
    intent_id = Column(Integer, ForeignKey("intents.intent_id"))
    example_text = Column(Text, nullable=False)
    is_main = Column(Boolean, default=False)
    embedding = Column(Text)  # Храним base64 для совместимости