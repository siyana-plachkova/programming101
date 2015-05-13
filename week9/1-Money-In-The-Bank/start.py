import getpass
import re
import hashlib
import time

from sql_manager import Database
from login_interface import LoginInterface
from password import Password
from exceptions import PasswordError
from blocked_users import BlockedUsers


class Interface:

    def __init__(self, database):
        self._database = database
        self._login_interface = LoginInterface(database)
        self._login_tries = 0
        self._block_users = BlockedUsers()

    @property
    def login_interface(self):
        return self._login_interface

    def main_menu(self):
        print("Welcome to our bank service. You are not logged in. \nPlease register or login")

        while True:
            command = input("$$$>")

            if command == 'register':
                self._register()
            elif command == 'login':
                self._login()
            elif command.startswith('send-reset-password'):
                username = command.split(' ')[1]
                self._send_reset_password(username)
            elif command == 'help':
                self._help()
            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def _validate_email(self, email):
        return bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email))

    def _register(self):
        entered_valid_username = False
        while not entered_valid_username:
            username = input("Enter your username: ").strip()

            if username:
                entered_valid_username = True
            else:
                print("The username is not valid.")

        entered_valid_email = False
        while not entered_valid_email:
            email = input("Enter your email: ")

            if not self._validate_email(email):
                print("Not a valid email. ")
            else:
                entered_valid_email = True

        entered_valid_pass = False
        while not entered_valid_pass:
            password = getpass.getpass(prompt='Enter your password: ')
            password = Password(password)

            try:
                password.check()
            except PasswordError as err:
                print(str(err))
            else:
                entered_valid_pass = True

        if entered_valid_username and entered_valid_email and entered_valid_pass:
            self._database.register(username, str(password))

            print("Registration Successfull")

    def _login(self):
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        password = Password(password)

        logged_user = self._database.login(username, str(password))

        if self._block_users.is_blocked(username):
            print("You are blocked")
        elif logged_user:
            self._login_tries = 0
            self.login_interface.show_menu(logged_user)
        else:
            self._login_tries += 1

            if self._login_tries >= 5:
                self._login_tries = 0
                self._block_users.block(username)
                print("You've entered your password wrong 5 times and now have to wait 5 minutes before your next login.")
            else:
                print("Login failed")

    def _send_reset_password(self, username):
        email = self._database.get_user_email(username)

        if not email:
            print("This user does not exist.")
        else:
            # concat  username, email and password (random)
            reset_string = username + email + time()
            # hash it (md5)
            hash_object = hashlib.md5(reset_string.encode("utf-8"))
            safety_hash_object = hash_object.hexdigest()
            # update the user in table with the reset pass hash
            self._database.update_reset_pass(safety_hash_object, username)
            # make a method sending email :D

    def _help(self):
        print("login - for logging in!")
        print("register - for creating new account!")
        print("exit - for closing program!")


def main():
    database = Database()
    database.create_clients_table()

    interface = Interface(database)
    interface.main_menu()

    database.close()

if __name__ == '__main__':
    main()
