# Бот для поддержки клиентов Дома с Маяком

## Features
- Распознавание вопросов с использованием эбендингов
- MySQL - интеграция с базой данных
- REST API - интеграция с веб-сайтом

## Local Development
1. Clone repo
2. `docker-compose up -d`
3. Access API at `http://localhost:5000`

## Production Deployment
1. Set environment variables:
   - `DB_HOST`, `DB_USER`, `DB_PASS`
   - `SECRET_KEY`
2. Deploy with Docker

## API Endpoints
POST `/api/ask` - Get answer for question