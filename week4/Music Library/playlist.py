import json
import random
from prettytable import PrettyTable

from song import Song, SongLength
from exceptions import SongAlreadyAdded, SongDoesNotExist, PlaylistEmpty


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        if not isinstance(name, str):
            raise TypeError("Invalid name argument. Expected string.")

        if not isinstance(repeat, bool):
            raise TypeError("Invalid repeat argument. Expected bool.")

        if not isinstance(shuffle, bool):
            raise TypeError("Invalid shuffle argument. Expected bool.")

        self._name = name
        self._repeat = repeat
        self._shuffle = shuffle
        self._songs = []

        self._played_songs = []
        self._current_song = None

    @property
    def name(self):
        return self._name

    @property
    def repeat(self):
        return self._repeat

    @property
    def shuffle(self):
        return self._shuffle

    @property
    def songs(self):
        return self._songs

    @property
    def current_song(self):
        current = [song for song in self._songs
                   if self._current_song == hash(song)]

        if len(current) == 0:
            return None

        return current[0]

    def add_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("Invalid song.")

        if song in self._songs:
            raise SongAlreadyAdded("The song is already in the playlist.")

        self._songs.append(song)

    def remove_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("Invalid song.")

        if song not in self._songs:
            raise SongDoesNotExist("The song is not in the playlist.")

        self._songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def length(self):
        seconds = sum([song.length(seconds=True) for song in self._songs])

        return str(SongLength.from_seconds(seconds))

    def artists(self):
        artists = [song.artist for song in self._songs]
        songs_count = [len(self._songs_by_artist(artist))
                       for artist in artists]

        return dict(zip(artists, songs_count))

    def next_song(self):
        if len(self._songs) == 0:
            raise PlaylistEmpty("No songs are added.")

        is_song_nonplayed = lambda song: hash(song) not in self._played_songs
        nonplayed_songs = list(filter(is_song_nonplayed, self._songs))

        if self._repeat and len(nonplayed_songs) == 0:
            self._played_songs = []
            nonplayed_songs = self._songs

        if self._shuffle and len(nonplayed_songs) != 1:
            first_song = nonplayed_songs[0]
            while nonplayed_songs[0] == first_song:
                random.shuffle(nonplayed_songs)

        song = None
        if len(nonplayed_songs) != 0:
            song = nonplayed_songs[0]
            self._current_song = hash(song)
            self._played_songs.append(self._current_song)
        else:
            self._played_songs = []
            self._current_song = None

        return song

    def choose_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("Invalid song.")

        self._played_songs = []
        self._current_song = hash(song)
        self._played_songs.append(self._current_song)

    def pprint_playlist(self, return_table=False):
        table = PrettyTable(["#", "Artist", "Song", "Length"])
        table.align["#"] = "l"

        song_index = 1
        for song in self._songs:
            table.add_row([song_index, song.artist, song.title, song.length()])
            song_index += 1

        if return_table:
            return table

        print(table)

    def save(self, json_filename):
        with open(json_filename, "w") as json_file:
            json_file.write(self._to_json())

    @staticmethod
    def load(json_filename):
        with open(json_filename, "r") as json_file:
            obj = json.load(json_file)

            playlist = Playlist(obj["_name"], obj["_repeat"], obj["_shuffle"])
            for song in obj["_songs"]:
                song_length = ("%d:%d:%d" % (song["_length"]["_hours"],
                                             song["_length"]["_minutes"],
                                             song["_length"]["_seconds"]))
                song_length_obj = SongLength(song_length)
                playlist.add_song(Song(song["_title"], song["_artist"],
                                       song["_album"], str(song_length_obj)))

            return playlist

    def _to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def _songs_by_artist(self, artist):
        return [song for song in self._songs if song.artist == artist]


def main():
    songs = []
    songs.append(Song(title="Odin", artist="Manowar",
                      album="The Sons of Odin", length="3:44"))
    songs.append(Song(title="Ghosts N Stuff", artist="deadmau5",
                      album="album title goes here", length="3:14"))
    songs.append(Song(title="Seeya", artist="deadmau5",
                      album="while(1<2)", length="6:40"))

    playlist = Playlist(name="Code", repeat=True, shuffle=True)
    playlist.add_songs(songs)
    playlist.pprint_playlist()
    playlist.save("test_json.json")
    playlist.load("test_json.json")

if __name__ == '__main__':
    main()
