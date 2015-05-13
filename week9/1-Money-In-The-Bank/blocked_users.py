from time import time


class BlockedUsers:

    def __init__(self):
        self._blocked = {}

    def block(self, username):
        self._blocked[username] = time()

    def unblock(self, username):
        self._blocked[username] = None

    def is_blocked(self, username):
        if username in self._blocked.keys() and self._blocked[username]:
            if time() - self._blocked[username] >= 60 * 5:
                self.unblock(username)
            else:
                return True

        return False
