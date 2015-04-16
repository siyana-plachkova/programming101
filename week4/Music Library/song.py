import time


class SongLength:

    def __init__(self, length):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0

        if not self._validate_length(length):
            raise ValueError("Length is not valid.")

    def _validate_length(self, length):
        length_list = [int(part.strip()) for part in length.split(':')]

        for iterator in range(0, len(length_list)):
            index = len(length_list) - iterator

            if index == 3:
                hours = length_list[iterator]
                if hours < 0 or 24 < hours:
                    return False

                self._hours = hours

            if index >= 2:
                minutes = length_list[iterator]
                if minutes < 0 or 59 < minutes:
                    return False

                self._minutes = minutes

            if index >= 1:
                seconds = length_list[iterator]
                if seconds < 0 or 59 < seconds:
                    return False

                self._seconds = seconds

        return True

    def to_hours(self):
        return self._hours

    def to_minutes(self):
        return self._hours * 60 + self._minutes

    def to_seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds

    def to_list(self):
        prepend_zero = lambda x: ("0" + str(x)) if x > 0 and x <= 9 else str(x)
        return [prepend_zero(part) for part in
                [self._hours, self._minutes, self._seconds]]

    @staticmethod
    def from_seconds(seconds):
        return SongLength(time.strftime("%H:%M:%S", time.gmtime(seconds)))

    def __str__(self):
        length_list = self.to_list()
        length = list(filter(lambda x: int(x) != 0, length_list))

        if len(length_list) >= 2 and int(length_list[-1]) == 0:
            length.append("00")

        return ':'.join(length).lstrip('0')

    def __repr__(self):
        return str(self)


class Song:

    def __init__(self, title, artist, album, length, path=None):
        if not isinstance(title, str):
            raise TypeError("Invalid title argument. Expected string.")

        if not isinstance(artist, str):
            raise TypeError("Invalid artist argument. Expected string.")

        if not isinstance(album, str):
            raise TypeError("Invalid album argument. Expected string.")

        if not isinstance(length, str):
            raise TypeError("Invalid length argument. Expected string.")

        self._title = title
        self._artist = artist
        self._album = album
        self._length = SongLength(length)
        self._path = path

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def album(self):
        return self._album

    @property
    def path(self):
        return self._path

    def length(self, hours=False, minutes=False, seconds=False):
        if hours:
            return self._length.to_hours()

        if minutes:
            return self._length.to_minutes()

        if seconds:
            return self._length.to_seconds()

        return str(self._length)

    def full_name(self):
        return ("%s - %s, %s" %
                (self._artist, self._title, self._length))

    def __str__(self):
        return ("%s - %s from %s - %s" %
                (self._artist, self._title, self._album, self._length))

    def __repr__(self):
        return str(self)

    def __eq__(self, other_song):
        return hash(self) == hash(other_song)

    def __hash__(self):
        return hash(str(self))
