class Client:

    def __init__(self, client_id, username, balance, message, email):
        self._username = username
        self._balance = balance
        self._id = client_id
        self._message = message
        self._email = email

    def get_username(self):
        return self._username

    def get_balance(self):
        return self._balance

    def get_id(self):
        return self._id

    def get_message(self):
        return self._message

    def set_message(self, new_message):
        self._message = new_message

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email
