# charity_bot/wsgi.py
from app import create_app
from app.config import Config

app = create_app(config_class=Config)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000)