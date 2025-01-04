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
    """Get user's playlists"""
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

def get_user_saved_tracks(limit=20):
    """Get user's saved tracks"""
    results = sp.current_user_saved_tracks(limit=limit)
    tracks = [
        {
            'name': item['track']['name'],
            'artist': item['track']['artists'][0]['name'],
            'album': item['track']['album']['name']
        }
        for item in results['items']
    ]
    return tracks
