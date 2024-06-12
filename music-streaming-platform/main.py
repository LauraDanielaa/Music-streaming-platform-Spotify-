"""
This module is the main entry point where web services are defined
to interact with all external users, including frontend clients
"""
import os
from fastapi import FastAPI
from pydantic import BaseModel, SecretStr
from dotenv import load_dotenv
from sqlalchemy import create_engine
from system import Playlist, Album, Artist, User
from command import Song, Action
from state import SubscribedUser, FreeUser




    

# db://user:password@url:port/name_db

app = FastAPI(
    title="Entertaininect",
    version="0.1",
    description="This is an api web to consume services for a entertaining center.",
)


@app.get("/heaaltcheck")
def healtcheck():
    """This is a service to validate web services are up."""
    return {
        "Message": "This is a healthcheck of entertaiment center project",
        "version": 1.0,
    }


class Login(BaseModel):
    username: str
    password: SecretStr



usuario = User(1, "juan", "sasa", "asas", "assa")

lau = Artist(1, "Laura", "Suba")

pallo = Artist(2, "Pallo", "fontibon")

song1 = Song("La cucaracha", 1)
song2 = Song("La cucharita", 2)
song3 = Song("La cucharona", 3)

song4 = Song("tienes un mensaje", 4)
song5 = Song("amor pasunchano", 5)
song6 = Song("himno", 6)

song7 = Song("metal", 7)
song8 = Song("rock", 8)
song9 = Song("uta", 9)

song10 = Song("carranga", 10)
song11 = Song("ballenato", 11)
song12 = Song("salsa", 12)

album1 = Album(1, "cuchara")
album2 = Album(2, "random")

album3 = Album(3, "rock")
album4 = Album(4, "tropical")

album1.add_song(song1)
album1.add_song(song2)
album1.add_song(song3)

album2.add_song(song4)
album2.add_song(song5)
album2.add_song(song6)

album3.add_song(song7) 
album3.add_song(song8)
album3.add_song(song9)

album4.add_song(song10)
album4.add_song(song11)
album4.add_song(song12)


lau.add_album(album1)
lau.add_album(album2)

pallo.add_album(album3)
pallo.add_album(album4)
 

# Services for Manager
@app.get("/manager/scheduling")
def watch_scheduling():
    """This service allows to a manager see full scheduling in the center."""
    return song1.play()

@app.get("/Lau/artist/albums")
def artist_albums():
    """This service allows to a manager see all albums of an artist."""
    return lau.get_albums()

@app.get("/Pallo/artist/albums")
def artist_albums():
    """This service allows to a manager see all albums of an artist."""
    return pallo.get_albums()

@app.get("/cuchara/album/songs")
def album_songs():
    """This service allows to a manager see all songs of an album."""
    return album1.get_songs()

@app.get("/random/album/songs")
def album_songs():
    """This service allows to a manager see all songs of an album."""
    return album2.get_songs()

@app.get("/rock/album/songs")
def album_songs():
    """This service allows to a manager see all songs of an album."""
    return album3.get_songs()

@app.get("/tropical/album/songs")
def album_songs():
    """This service allows to a manager see all songs of an album."""
    return album4.get_songs()




