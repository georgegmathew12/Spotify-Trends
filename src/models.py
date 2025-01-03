from database import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)

    def __repr__(self):
        return f'<Artist {self.name}>'

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

    artist = db.relationship('Artist', back_populates='albums')

    def __repr__(self):
        return f'<Album {self.title}>'

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    duation = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    album = db.relationship('Album', back_populates='tracks')

    def __repr__(self):
        return f'<Track {self.title}>'

Artist.albums = db.relationship('Album', back_populates='artist', cascade='all, delete-orphan')
Album.tracks = db.relationship('Track', back_populates='album', cascade='all, delete-orphan')
