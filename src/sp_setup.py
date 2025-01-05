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
token_info = auth_manager.get_access_token()
access_token = token_info['access_token']
