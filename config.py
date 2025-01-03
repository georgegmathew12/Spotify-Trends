import os
from dotenv import load_dotenv

load_dotenv() # Load environment vars from .env

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    CID = os.getenv('CID')
    SECRET = os.getenv('SECRET')

    @staticmethod
    def validate_config():
        """Ensure valid config variables are set"""
        if not Config.SQLALCHEMY_DATABASE_URI:
            raise ValueError("Database URI not set in .env")
        if not Config.CID or not Config.SECRET:
            raise ValueError("CID or SECRET not set in .env")
