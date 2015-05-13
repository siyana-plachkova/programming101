import re
import hashlib

from exceptions import PasswordError


class Password:

    def __init__(self, password):
        self._password = password

    def check(self):
        if len(self._password) < 8:
            raise PasswordError("Password too short! Must be at least 8 symbols.")

        if not re.search('[a-zA-Z]', self._password):
            raise PasswordError("Your password must contain upper and lower case characters!")

        if not re.search('[0-9]', self._password):
            raise PasswordError("Your password must contain digits!")

        if not re.search('[^a-zA-Z0-9]', self._password):
            raise PasswordError("Your password must contain special symbols!")

    def __str__(self):
        return self.hash()

    def __repr__(self):
        return self.hash()

    def hash(self):
        hash_object = hashlib.sha1(self._password.encode("utf-8"))
        return hash_object.hexdigest()
