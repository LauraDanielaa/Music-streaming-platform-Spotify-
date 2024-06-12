class Receiver:
    """Receiver class responsible for playing the song."""

    def play(self):
        """Play the song."""
        return "La canción sonando es"

class Command:
    """Command class that defines the interface for all commands."""

    def play(self):
        """Play command to be implemented by concrete commands."""
        pass

class Song(Command):
    """Song class that represents a song and implements the play command."""

    def __init__(self, song_name, duration_song):
        """Initialize a new song."""
        self.receiver = Receiver()
        self.song_name = song_name
        self.duration_song = duration_song
        self.like = False

    def play(self):
        """Play the song."""
        return self.receiver.play() + " " +  self.song_name



class Action:
    """Action class that invokes the command."""

    def __init__(self, song):
        """Initialize a new action with a song."""
        self.song = song

    def press(self):
        """Invoke the play command on the song."""
        return self.song.play()