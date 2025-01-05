import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import Config
import os

scope = "user-library-read user-top-read user-follow-read user-read-private playlist-read-private"
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

def get_user_info(time_range='short_term'):
    """ Get user's information"""
    user = sp.current_user()
    user_profile = {
        'display_name':user['display_name'],
        'profile_image':user['images'][0]['url'] if user.get('images') else None,
        'follower_count':user['followers']['total'],
    }
    top_tracks = get_user_top_tracks(time_range)
    top_artists = get_user_top_artists(time_range)
    user_info = {
        'user':user_profile,
        'top_tracks':top_tracks,
        'top_artists':top_artists
    }
    return user_info

def get_user_top_tracks(time_range='short_term', limit=20):
    """Get user's top tracks"""
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    top_tracks = [
        {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name']
        }
        for item in results['items']
    ]
    return top_tracks

def get_user_top_artists(time_range='short_term', limit=20):
    """Get user's top artists"""
    results = sp.current_user_top_artists(time_range=time_range, limit=limit)
    top_artists = [
        {
            'name': item['name'],
            'genres': item['genres'][:3],
            'popularity': item['popularity']
        }
        for item in results['items']
    ]
    return top_artists
