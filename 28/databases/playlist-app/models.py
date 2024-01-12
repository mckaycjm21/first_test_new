"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    
def create_all(app):
    with app.app_context():
        db.create_all()
        
        
class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    
    def __repr__(self):
        p = self
        return f"<Playlist ID = {p.id} Name = {p.name} Playlist Description = {p.description}>"

    id = db.Column(db.Integer,
                   autoincrement = True,
                   primary_key = True)
    name = db.Column(db.String,
                     nullable = False)
    description = db.Column(db.String,
                            nullable = True)
    songs = db.relationship('Song', 
                            secondary = 'playlist_songs',
                            backref = 'playlists')
    playlistsong = db.relationship('PlaylistSong',
                                   backref = "playlists")


class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    
    def __repr__(self):
        p = self
        return f"<Song ID = {p.id} Title = {p.title} Artist = {p.artist}>"

    id = db.Column(db.Integer,
                   autoincrement = True,
                   primary_key = True)
    title = db.Column(db.String,
                     nullable = False)
    artist = db.Column(db.String,
                            nullable = False)
    playlistsong = db.relationship('PlaylistSong',
                                   backref = "songs")



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlist_songs'

    def __repr__(self):
        p = self
        return f"<PlaylistSong ID = {p.id}  = {p.playlist_id} Playlist Description = {p.song_id}>"

    playlist_id = db.Column(db.Integer,
                            db.ForeignKey("playlists.id"),
                            primary_key = True)
    song_id= db.Column(db.Integer,
                       db.ForeignKey("songs.id"),
                       primary_key = True)