import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from config import Config
from database import db
from models import Artist, Album, Track
from data_collection import sp, get_user_playlists, get_user_saved_tracks, get_user_info

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

@app.route('/')
def user_info():
    try:
        user_info = get_user_info()
        return render_template('profile.html', user_info=user_info)
    except Exception as e:
        return f'Error: {e}'

@app.route('/playlists')
def playlists():
    try:
        playlists = get_user_playlists()
        return render_template('playlists.html', playlists=playlists)
    except Exception as e:
        return f'Error: {e}'

@app.route('/saved_tracks')
def saved_tracks():
    try:
        tracks = get_user_saved_tracks()
        return render_template('saved_tracks.html', tracks=tracks)
    except Exception as e:
        return f'Error: {e}'

@app.route('/top_tracks')
def top_tracks():
    try:
        top_tracks = get_user_top_tracks()
        return render_template('top_tracks.html', top_tracks=top_tracks)
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run()
