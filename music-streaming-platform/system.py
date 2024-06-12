from state import SubscribedUser, FreeUser
from command import Song, Action

class Playlist:
    """A playlist of liked songs."""

    def __init__(self, name):
        """Initialize a new playlist."""
        self.name = name
        self.song_list = []

    def add_song(self, song):
        """Add a song to the playlist."""
        self.song_list.append(song)

    def get_songs(self):
        """Return the names of all songs in the album."""
        return [song.song_name for song in self.song_list]


class Album:
    """An album by an artist."""

    def __init__(self, id_artist, album_name):
        """Initialize a new album."""
        self.song_list = []
        self.id_artist = id_artist
        self.album_name = album_name
    
    def add_song(self, song):
        """Add a song to the album."""
        self.song_list.append(song)

    def get_songs(self):
        """Return the names of all songs in the album."""
        return [song.song_name for song in self.song_list]
        

class Artist:
    """An artist who creates music."""

    def __init__(self, id_artist, artist_name, city_of_origin):
        """Initialize a new artist."""
        self.album_list = []
        self.id_artist = id_artist
        self.artist_name = artist_name
        self.city_of_origin = city_of_origin

    
    def get_albums(self):
        """Return the names of all albums by the artist."""
        return [album.album_name for album in self.album_list]
    def add_album(self, album):
        """Add an album to the artist."""
        self.album_list.append(album)


class User:
    """A user of the music service."""

    def __init__(self, id_user, user_name, password, email, musical_genre_tastes):
        """Initialize a new user."""
        self.id_user = id_user
        self.user_name = user_name
        self.password = password
        self.email = email
        self.playlists = []