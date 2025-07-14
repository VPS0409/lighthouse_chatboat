# app/api/endpoints.py
from flask import Blueprint, request, jsonify
from app.services.bot_service import CharityBot

bp = Blueprint('api', __name__)
bot = CharityBot()

@bp.route('/add_question', methods=['POST'])
def add_question():
    data = request.json
    bot.add_complete_question(
        main_question=data['question'],
        answer_text=data['answer'],
        variations=data.get('variations', [])
    )
    return jsonify({"status": "success"})