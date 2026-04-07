import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'bca-student-ai-secret-2024')

    # ── AWS RDS PostgreSQL ─────────────────────────────────────────────────────
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASS = os.getenv('DB_PASS')
    DB_NAME = os.getenv('DB_NAME', 'student_performance_db')

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASS}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,       # auto-reconnect if connection drops
        'pool_recycle':  300,        # recycle connections every 5 min
        'connect_args': {
            'connect_timeout': 10,   # 10 second connection timeout
        }
    }
