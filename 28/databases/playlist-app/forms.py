"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name")
    description = StringField("Description")


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title")
    artist = StringField("Artist Name")


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
