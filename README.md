# Course Project - Music Streaming Platform - Spotify

we developed a music playback website with some functionalities and certain similarities to one of the most known platforms worldwide, Spotify, in which several users with free or subscribed accounts can listen to music. To achieve this and to have a good realization and structure of the software we took into account patterns, antipatterns, code smells, solid principles and crude operations.

## Business model

You have to access a music playback page where users log in by means of a login, in which their contact information is registered and stored in a database. On this music site users can have a free account or a subscription account. Subscription account users have additional features that a free user does not have, such as playing music without ads, being able to rewind songs and being able to shuffle music in a playlist. 
If a user wants to be an artist there has to be a settings menu in which he can be an artist. He will have to add his data and upload an album with songs so that he can be considered as an artist. 

### Business rules 
- Songs may not be longer that 5 minutes 
- You want a person who wants to enter the music platform to have two options, a log in or a sign up.
- If the person indicates that he/she wants to log in because he/she already has a registered account, the system verifies that the account has been registered before. 
- If the person indicates to register the system saves the data provided by the user. 
- There are two types of users, a free user and a subscribed user. The user becomes a subscriber when he/she makes a monthly payment to the platform, which provides certain benefits, such as listening to music without ads, returning songs and playing songs from a playlist randomly. 
- When a user wants to become an artist he goes to a menu of options in which he indicates his artist data and has to upload an album with songs. 
A user (no matter in which state he is) can make a playList with the songs he likes. 
  

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
