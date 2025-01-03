import os
from dotenv import load_dotenv

load_dotenv() # Load environment vars from .env

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    CID = os.getenv('CID')
    SECRET = os.getenv('SECRET')

print(os.getenv('DB_URI'))
