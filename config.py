import os
from dotenv import load_dotenv

load_dotenv() # Load environment vars from .env

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')

    @staticmethod
    def validate_config():
        """Ensure valid config variables are set"""
        if not Config.SQLALCHEMY_DATABASE_URI:
            raise ValueError("Database URI not set in .env")
