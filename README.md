# Course Project - Music Streaming Platform - Spotify

This project is a course example to create a backend system _using object-oriented design_, _design patterns_ and some _good code practices_ in order to provide a __RESTful API__ with different services related to music, podcasts and it is author in a comfortable platform.

## Business model

This is a music streaming platform where users can login from a web platform to listen to music, podcast, follow favorite artists and singers, save music and podcast and make playlist 

### Business rules 
- Songs may not be longer that 10 minutes 
- To login you need to have a username and a password 
- There can not be repeated user names
  

## User Stories

- __As a__ _artist_, __I want__ to see all reproductions of my songs, __so what__ see the best songs.
- __As a__ _listener_, __I want__ to listen to any songs available,  __so what__ see new songs.
- __As a__ _listener_, __I want__ create a playlist with songs, __so what__ listen to my favorite songs one after another.
- __As a__ _listener_, __I want__ like and save a song, __so what__ listen to my favorite music without searching for them.
- __As a__ _artist_, __I want__ upload and delete my songs, __so what__ show my songs and remove them.
- __As a__ _artist_, __I want__ create albums with my songs, __so what__.

## Technical definitions

### tools to Use

In this case, the backend will be build using _pytohn 3.11.0_, and some related technologies as _Pytest_ to apply some simple unit test, and _Black_ to auto-format the code and increase code readability.


## Entities
- __User__: name, id, email, password, login(), logout(), search(),play(), singup()
- __listener(User)__: like(), add, create_playlist()[E]
- __artist(User)__: upload(), delete()
- __song__: name, duration, artist[E], musical genre, upload(), delete()
- __playlist__: len, duration, song[E]
- __album__: name, song[E]
- __subscription__: price, duration

# Processes
- Create a Playlist
- Create a Playlist
- Search songs 
- give like
- listen songs
- upload song
- delete song
