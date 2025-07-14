# app/database/crud.py
from .models import Intent, Answer, IntentExample
from .session import SessionLocal

def initialize_database(db_config):
    """Создает таблицы в БД (вызывается один раз при первом запуске)"""
    from .models import Base
    engine = create_engine(db_config['SQLALCHEMY_DATABASE_URI'])
    Base.metadata.create_all(bind=engine)

def add_new_question(intent_name: str, answer_text: str, examples: list):
    """Добавляет новый вопрос с вариациями и ответом"""
    db = SessionLocal()
    try:
        # 1. Добавляем ответ
        answer = Answer(answer_text=answer_text)
        db.add(answer)
        db.commit()
        
        # 2. Добавляем интент
        intent = Intent(intent_name=intent_name, answer_id=answer.answer_id)
        db.add(intent)
        db.commit()
        
        # 3. Добавляем примеры
        for example in examples:
            db_example = IntentExample(
                intent_id=intent.intent_id,
                example_text=example
            )
            db.add(db_example)
        db.commit()
        
    finally:
        db.close()