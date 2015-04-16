import os
import urwid
urwid.set_encoding("UTF-8")
from time import time
from subprocess import Popen, PIPE

from song import SongLength
from crawler import MusicCrawler

TITLE = "MUSIC PLAYER"
VERSION = "1.0"
COMMAND = "afplay"


class SongPlay:

    def __init__(self, song):
        self._song = song
        self._process = None
        self._start_time = time()

    @property
    def song(self):
        return self._song

    def play(self):
        if self._song is None:
            return

        command = [COMMAND, self._song.path]
        self._process = Popen(command, stdout=PIPE, stderr=PIPE)

    def stop(self):
        self._process.kill()

    def elapsed_time(self, humanized=False):
        elapsed = time() - self._start_time

        if humanized:
            return str(SongLength(elapsed))

        return elapsed

    def has_stopped(self):
        if self._song.length(seconds=True) <= self.elapsed_time():
            return True

        return False


class MusicPlayer:

    _palette = [
        (None, 'light gray', 'black'),
        ('heading', 'black', 'light gray'),
        ('line', 'black', 'light gray'),
        ('options', 'dark gray', 'black'),
        ('focus heading', 'white', 'dark red'),
        ('focus line', 'black', 'dark red'),
        ('focus options', 'black', 'light gray'),
        ('selected', 'white', 'dark blue'),
        ('edit', 'bold', 'black', 'bold')
    ]

    def __init__(self):
        self._playlist = None
        self._music_directory = None
        self._music_playing = False
        self._currently_playing = None

        self._ui = urwid.raw_display.Screen()
        self._ui.register_palette(self._palette)
        self._build_ui()
        self._ui.run_wrapper(self._run)

    def _run(self):
        self._main_loop = urwid.MainLoop(self._context,
                                         screen=self._ui,
                                         unhandled_input=self.exit)

        def call_redraw(*x):
            self._main_loop.draw_screen()

            self._refresh_player()

            if self._invalidate_ui:
                self._invalidate_ui = False
                self._draw_ui()

            invalidate.locked = False
            return True

        inv = urwid.canvas.CanvasCache.invalidate

        def invalidate(cls, *a, **k):
            inv(*a, **k)

            if not invalidate.locked:
                invalidate.locked = True
                self._main_loop.set_alarm_in(0, call_redraw)

        invalidate.locked = False
        urwid.canvas.CanvasCache.invalidate = classmethod(invalidate)

        try:
            self._main_loop.run()
            self.start()
        except KeyboardInterrupt:
            self.exit()

    def start(self):
        self._draw_ui()

    def play(self):
        if self._currently_playing:
            if self._currently_playing.song != self._playlist.current_song:
                self.stop()
            else:
                return

        if self._playlist.current_song is None:
            self._playlist.next_song()

        self._currently_playing = SongPlay(self._playlist.current_song)
        self._currently_playing.play()

        self._music_playing = True

        self._redraw_ui()

    def stop(self, no_redraw=False):
        if self._currently_playing:
            self._currently_playing.stop()
            self._currently_playing = None

        self._music_playing = False

        if no_redraw:
            return

        self._redraw_ui()

    def next(self):
        self._playlist.next_song()

        if self._playlist.current_song is not None:
            self.play()
        else:
            self.stop()

    def exit(self, button='q'):
        if button == 'q':
            self._music_directory = None
            self.stop(no_redraw=True)
            raise urwid.ExitMainLoop()
        elif button == 'n':
            self.next()
        elif button == 's':
            self.stop()
        elif button == 'p':
            self.play()

    def _build_ui(self):
        self._invalidate_ui = True
        self._main_window = urwid.Padding(
            urwid.ListBox(self._title()),
            left=2, right=2
        )
        self._context = urwid.Overlay(
            self._main_window,
            urwid.SolidFill(u'\N{MEDIUM SHADE}'),
            align='center', width=('relative', 60),
            valign='middle', height=('relative', 50),
            min_width=40, min_height=30
        )

    def _draw_ui(self):
        if not self._music_playing and not self._music_directory:
            self._draw_initial_options()
        elif self._music_directory:
            self._draw_playlist_options()

    def _redraw_ui(self):
        self._invalidate_ui = True
        self._draw_ui()

    def _draw_initial_options(self):
        subtitle = "Music directory"

        directory_edit = urwid.Edit(("edit", "Enter playlist directory:\n"))
        status_textblock = urwid.Text("")
        done_button = urwid.Button('Done')

        def on_directory_change(edit, new_edit_text):
            self._music_directory = new_edit_text.replace('\ ', ' ')
            status_textblock.set_text("")

        def directory_submit(button):
            if not os.path.isdir(self._music_directory):
                status_textblock.set_text("Entered directory is not valid!")
            else:
                crawler = MusicCrawler(self._music_directory)
                self._playlist = crawler.generate_playlist()
                self._redraw_ui()

        urwid.connect_signal(done_button, 'click', directory_submit)
        urwid.connect_signal(directory_edit, 'change', on_directory_change)

        content = [directory_edit, status_textblock, done_button]
        self._update_content(self._create_listbox(content, subtitle))

    def _draw_playlist_options(self):
        subtitle = ("Music playlist: '" + self._playlist.name + "'" +
                    "\nTotal playtime: " + self._playlist.length())

        content = []

        def click_song(button, song):
            self._playlist.choose_song(song)
            self.play()

        for song in self._playlist.songs:
            button_text = song.full_name()
            if (self._currently_playing and
                    self._currently_playing.song == song):
                button_text = ("bold", chr(9658) + " " + song.full_name())

            button = urwid.Button(button_text)
            urwid.connect_signal(button, 'click', click_song, song)
            content.append(urwid.AttrMap(button, None, focus_map='reversed'))

        content.append(urwid.Divider())

        self._update_content(self._create_listbox(content, subtitle))

    def _title(self, subtitle=None):
        title = "%s v%s" % (TITLE, VERSION)
        title_ui = urwid.AttrMap(urwid.Text(title, align="center"), 'heading')
        title_body = [title_ui]

        if subtitle:
            subtitle_ui = urwid.AttrMap(urwid.Text(subtitle, align="center"),
                                        'selected')
            title_body.append(subtitle_ui)

        title_body.append(urwid.Divider())

        return title_body

    def _create_listbox(self, elements, subtitle=None):
        body = self._title(subtitle)

        body.extend(elements)

        button = urwid.Button('Exit')
        urwid.connect_signal(button, 'click', lambda x: self.exit('q'))
        body.extend([button, urwid.Divider()])

        return urwid.ListBox(urwid.SimpleFocusListWalker(body))

    def _update_content(self, content):
        self._main_window.original_widget = content

    def _refresh_player(self):
        if self._currently_playing and self._currently_playing.has_stopped():
            self.next()


def main():
    music_player = MusicPlayer()
    music_player.start()

if __name__ == '__main__':
    main()
