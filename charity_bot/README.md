# Charity Bot for Medical Support

## Features
- Intent recognition with multilingual embeddings
- MySQL database integration
- REST API for website integration

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