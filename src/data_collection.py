from sp_setup import sp
from collections import Counter

# User Profile Functions
def get_user_profile(time_range):
    user_info = get_user_info(time_range)
    top_tracks = get_user_top_tracks(time_range)
    top_artists = get_user_top_artists(time_range)
    top_genres = get_user_top_genres(time_range)

    user_profile = {
        'user':user_info,
        'top_tracks':top_tracks,
        'top_artists':top_artists,
        'top_genres':top_genres
    }
    return user_profile

def get_user_info(time_range):
    """ Get user's information"""
    user = sp.current_user()
    user_info = {
        'display_name':user['display_name'],
        'profile_image':user['images'][0]['url'] if user.get('images') else None,
        'follower_count':user['followers']['total'],
    }
    return user_info

def get_user_top_tracks(time_range):
    """Get user's top tracks"""
    results = sp.current_user_top_tracks(time_range=time_range)
    top_tracks = [
        {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name']
        }
        for item in results['items']
    ]
    return top_tracks

def get_user_top_artists(time_range):
    """Get user's top artists"""
    results = sp.current_user_top_artists(time_range=time_range)
    top_artists = [
        {
            'name': item['name'],
            'genres': item['genres'],
            'popularity': item['popularity']
        }
        for item in results['items']
    ]
    return top_artists

def get_user_top_genres(time_range):
    top_artists = get_user_top_artists(time_range)
    genres = [genre for artist in top_artists for genre in artist['genres']]
    genre_counts = Counter(genres)
    top_genres = genre_counts.most_common(10)
    return top_genres

# Music Recommendation Functions
def get_user_recommendations():
    """Get user's track recommendations"""
    user_top_tracks = sp.current_user_top_tracks(time_range='short_term')
    user_top_track_ids = [str(track['id']) for track in user_top_tracks['items']]
    results = sp.recommendations(seed_tracks=user_top_track_ids[:5])
    recommended_tracks = [
        {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name']
        }
        for item in results['items']
    ]
    return recommended_tracks
