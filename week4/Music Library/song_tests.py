import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self._song = Song(title="Odin", artist="Manowar",
                          album="The Sons of Odin", length="3:44")

    def test_init(self):
        self.assertTrue(isinstance(self._song, Song))

        with self.assertRaises(ValueError):
            Song(title="Odin", artist="Manowar",
                 album="The Sons of Odin", length=":44")

        with self.assertRaises(TypeError):
            Song(title=0, artist="Manowar",
                 album="The Sons of Odin", length="3:44")

        with self.assertRaises(TypeError):
            Song(title="Odin", artist=0,
                 album="The Sons of Odin", length="3:44")

        with self.assertRaises(TypeError):
            Song(title="Odin", artist="Manowar",
                 album=0, length="3:44")

        with self.assertRaises(TypeError):
            Song(title="Odin", artist="Manowar",
                 album="The Sons of Odin", length=0)

    def test_str(self):
        valid_str = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(str(self._song), valid_str)

    def test_eq(self):
        same_song = Song(title="Odin", artist="Manowar",
                         album="The Sons of Odin", length="3:44")
        self.assertEqual(self._song, same_song)

    def test_hash(self):
        self.assertEqual(hash(self._song), hash(str(self._song)))

    def test_length(self):
        self.assertEqual(self._song.length(), "3:44")

    def test_length_seconds(self):
        self.assertEqual(self._song.length(seconds=True), 224)

    def test_length_minutes(self):
        self.assertEqual(self._song.length(minutes=True), 3)

    def test_length_hours(self):
        self.assertEqual(self._song.length(hours=True), 0)

if __name__ == '__main__':
    unittest.main()
