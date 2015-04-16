import os
from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.easyid3 import EasyID3

from exceptions import SongAlreadyAdded
from song import Song, SongLength
from playlist import Playlist


class MusicCrawler:

    def __init__(self, music_directory):
        if not os.path.isdir(music_directory):
            raise ValueError("Music directory does not exist.")

        self._music_directory = music_directory.replace('\ ', ' ')

    def generate_playlist(self):
        playlist_name = os.path.basename(self._music_directory.rstrip('/'))
        playlist = Playlist(playlist_name)

        for dirpath, dirnames, filenames in os.walk(self._music_directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                name, extension = os.path.splitext(filepath)
                if os.path.isfile(filepath) and extension == ".mp3":
                    try:
                        song = self._create_song(filepath)
                        playlist.add_song(song)
                    except HeaderNotFoundError:
                        continue
                    except SongAlreadyAdded:
                        continue

        return playlist

    def _create_song(self, songpath):
        audio = MP3(songpath, ID3=EasyID3)

        audio_title = audio.get('title')
        title = ((audio_title[0]
                  if isinstance(audio_title, list)
                  else audio_title)
                 if audio_title is not None else '')

        audio_artist = audio.get('artist')
        artist = ((audio_artist[0]
                   if isinstance(audio_artist, list)
                   else audio_artist)
                  if audio_artist is not None else '')

        audio_album = audio.get('album')
        album = ((audio_album[0]
                  if isinstance(audio_album, list)
                  else audio_album)
                 if audio_album is not None else '')

        audio_length = int(audio.info.length)
        length = str(SongLength.from_seconds(audio_length))

        return Song(title, artist, album, length, songpath)


def main():
    crawler = MusicCrawler("./music")
    playlist = crawler.generate_playlist()
    playlist.pprint_playlist()

if __name__ == '__main__':
    main()
