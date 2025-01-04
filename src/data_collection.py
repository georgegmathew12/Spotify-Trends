import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import Config
import os

scope = 'user-library-read'
client_id = os.getenv('CID')
client_secret = os.getenv('SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
auth_manager = SpotifyOAuth(
    scope=scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri
)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_user_playlists(limit=20):
    user = sp.current_user()
    user_id = user['id']
    results = sp.user_playlists(user=user_id, limit=limit)
    playlists = [
        {
            'name': item['name'],
            'description': item['description'],
            'url': item['external_urls']['spotify']
        }
        for item in results['items']
    ]
    return playlists
