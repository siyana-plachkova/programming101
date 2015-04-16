import os
import json
import unittest

from song import Song
from playlist import Playlist
from exceptions import SongAlreadyAdded, SongDoesNotExist, PlaylistEmpty


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self._playlist = Playlist(name="Code", repeat=True, shuffle=True)

        self._songs = []
        self._songs.append(Song(title="Odin", artist="Manowar",
                                album="The Sons of Odin", length="3:44"))
        self._songs.append(Song(title="Ghosts N Stuff", artist="deadmau5",
                           album="album title goes here", length="3:14"))
        self._songs.append(Song(title="Seeya", artist="deadmau5",
                           album="while(1<2)", length="6:40"))

    def test_init(self):
        self.assertTrue(isinstance(self._playlist, Playlist))

        with self.assertRaises(TypeError):
            Playlist(name=0, repeat=True, shuffle=True)

        with self.assertRaises(TypeError):
            Playlist(name="Code", repeat="", shuffle=True)

        with self.assertRaises(TypeError):
            Playlist(name="Code", repeat=True, shuffle="")

    def test_add_song(self):
        self.assertEqual(len(self._playlist.songs), 0)
        self._playlist.add_song(self._songs[0])
        self.assertEqual(len(self._playlist.songs), 1)

        with self.assertRaises(SongAlreadyAdded):
            self._playlist.add_song(self._songs[0])

        with self.assertRaises(TypeError):
            self._playlist.add_song(0)

    def test_remove_song(self):
        with self.assertRaises(SongDoesNotExist):
            self._playlist.remove_song(self._songs[0])

        with self.assertRaises(TypeError):
            self._playlist.remove_song(0)

        self.assertEqual(len(self._playlist.songs), 0)
        self._playlist.add_song(self._songs[0])
        self.assertEqual(len(self._playlist.songs), 1)
        self._playlist.remove_song(self._songs[0])
        self.assertEqual(len(self._playlist.songs), 0)

    def test_add_songs(self):
        self.assertEqual(len(self._playlist.songs), 0)
        self._playlist.add_songs(self._songs)
        self.assertEqual(len(self._playlist.songs), 3)

        with self.assertRaises(SongAlreadyAdded):
            self._playlist.add_songs(self._songs)

    def test_total_length(self):
        self.assertEqual(len(self._playlist.songs), 0)
        self._playlist.add_songs(self._songs)
        self.assertEqual(len(self._playlist.songs), 3)

        self.assertEqual(self._playlist.length(), "13:38")

    def test_artists(self):
        self._playlist.add_songs(self._songs)
        artists_histogram = self._playlist.artists()

        self.assertEqual(len(artists_histogram), 2)
        self.assertEqual(sum(artists_histogram.values()), 3)
        self.assertEqual(artists_histogram["deadmau5"], 2)

    def test_next_song(self):
        with self.assertRaises(PlaylistEmpty):
            self._playlist.next_song()

        no_shuffle_playlist = Playlist(name="Code", repeat=True, shuffle=False)
        no_repeat_playlist = Playlist(name="Code", repeat=False, shuffle=False)

        self._playlist.add_songs(self._songs)
        no_shuffle_playlist.add_songs(self._songs)
        no_repeat_playlist.add_songs(self._songs)

        self.assertEqual(self._playlist.current_song, None)
        self.assertEqual(no_shuffle_playlist.current_song, None)
        self.assertEqual(no_repeat_playlist.current_song, None)

        self._playlist.next_song()
        no_shuffle_playlist.next_song()
        no_repeat_playlist.next_song()

        self.assertNotEqual(self._playlist.current_song,
                            no_shuffle_playlist.current_song)
        self.assertNotEqual(self._playlist.current_song,
                            no_repeat_playlist.current_song)
        self.assertEqual(no_shuffle_playlist.current_song,
                         no_repeat_playlist.current_song)

        self._playlist.next_song()
        no_shuffle_playlist.next_song()
        no_repeat_playlist.next_song()

        self.assertEqual(no_shuffle_playlist.current_song,
                         no_repeat_playlist.current_song)

        self._playlist.next_song()
        no_shuffle_playlist.next_song()
        no_repeat_playlist.next_song()

        self.assertEqual(no_shuffle_playlist.current_song,
                         no_repeat_playlist.current_song)

        self._playlist.next_song()
        no_shuffle_playlist.next_song()
        no_repeat_playlist.next_song()

        self.assertNotEqual(no_shuffle_playlist.current_song,
                            no_repeat_playlist.current_song)
        self.assertNotEqual(self._playlist.current_song, None)
        self.assertNotEqual(no_shuffle_playlist.current_song, None)
        self.assertEqual(no_repeat_playlist.current_song, None)

        self._playlist.next_song()
        no_shuffle_playlist.next_song()
        no_repeat_playlist.next_song()

        self.assertNotEqual(self._playlist.current_song, None)
        self.assertNotEqual(no_shuffle_playlist.current_song, None)
        self.assertNotEqual(no_repeat_playlist.current_song, None)

    def test_save(self):
        test_filename = "test.json"
        self._playlist.add_songs(self._songs)
        self._playlist.save(test_filename)

        with open(test_filename, "r") as json_file:
            obj = json.load(json_file)

            self.assertEqual(len(obj["_songs"]), len(self._playlist.songs))

        os.unlink(test_filename)

    def test_load(self):
        test_filename = "test.json"
        self._playlist.add_songs(self._songs)
        self._playlist.save(test_filename)

        loaded_playlist = Playlist.load(test_filename)
        playlist_table = self._playlist.pprint_playlist(return_table=True)
        loaded_table = loaded_playlist.pprint_playlist(return_table=True)
        self.assertEqual(str(playlist_table), str(loaded_table))

        os.unlink(test_filename)


if __name__ == '__main__':
    unittest.main()
