import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from config import Config
from database import db, init_db
from models import Artist, Album, Track

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Tables created successfully'

if __name__ == '__main__':
    app.run()
