import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from config import Config
from database import db
from models import Artist, Album, Track
from data_collection import sp, get_user_profile, get_user_recommendations

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def user_info():
    try:
        time_range = request.args.get('time_range', 'short_term')
        user_profile = get_user_profile(time_range)
        return render_template('profile.html', user_profile=user_profile, time_range=time_range)
    except Exception as e:
        return f'Error: {e}'

# @app.route('/recommendations')
# def recommendations():
#     try:
#         recommended_tracks = get_user_recommendations()
#         return render_template('recommendations.html', recommended_tracks=recommended_tracks)
#     except Exception as e:
#         return f'Error: {e}'

if __name__ == '__main__':
    app.run()
