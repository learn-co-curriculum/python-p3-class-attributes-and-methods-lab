#!/usr/bin/env python3

from song import Song

class TestSong:
    '''Class "Song" in song.py'''

    Song("99 Problems", "Jay Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert(out_of_touch.name == "Out of Touch")
        assert(out_of_touch.artist == "Hall and Oates")
        assert(out_of_touch.genre == "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        assert(Song.count == 4)
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.count == 5)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        assert("Rap" in Song.genres)
        assert("Pop" in Song.genres)
        assert("Rock" in Song.genres)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        assert("Jay Z" in Song.artists)
        assert("Beyonce" in Song.artists)
        assert("Hall and Oates" in Song.artists)
        
    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        assert(Song.genre_count["Rap"] == 1)
        assert(Song.genre_count["Pop"] == 3)
        assert(Song.genre_count["Rock"] == 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        assert(Song.artist_count.get("Jay Z") == 1)
        assert(Song.artist_count.get("Beyonce") == 1)
        assert(Song.artist_count.get("Nirvana") == 1)
        assert(Song.artist_count.get("Hall and Oates") == 2)