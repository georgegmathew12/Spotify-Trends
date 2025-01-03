from database import db

class Artist(db.Model):
    """Represents an artist in the database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)

    albums = db.relationship('Album', back_populates='artist', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Artist {self.name}>'

class Album(db.Model):
    """Represents an album in the database"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

    artist = db.relationship('Artist', back_populates='albums')
    tracks = db.relationship('Track', back_populates='album', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Album {self.title}>'

class Track(db.Model):
    """Represents a track in the database"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    album = db.relationship('Album', back_populates='tracks')

    def __repr__(self):
        return f'<Track {self.title}>'
