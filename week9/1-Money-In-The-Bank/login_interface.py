import getpass
from password import Password
from exceptions import PasswordError


class LoginInterface:

    def __init__(self, database):
        self._database = database
        self._logged_user = None

    @property
    def logged_user(self):
        return self._logged_user

    def show_menu(self, logged_user):
        self._logged_user = logged_user
        print("Welcome you are logged in as: " + self.logged_user.get_username())

        while True:
            command = input("Logged>>")

            if command == 'info':
                self._info()
            elif command == 'changepass':
                self._change_pass()
            elif command == 'change-message':
                self._change_message()
            elif command == 'show-message':
                self._show_message()
            elif command == 'help':
                self._help()

    def _info(self):
        print("You are: " + self.logged_user.get_username())
        print("Your id is: " + str(self.logged_user.get_id()))
        print("Your balance is:" + str(self.logged_user.get_balance()) + '$')

    def _change_pass(self):
        new_pass = None

        entered_valid_pass = False
        while not entered_valid_pass:
            new_pass = getpass.getpass(prompt="Enter your new password: ")
            new_pass = Password(new_pass)

            try:
                new_pass.check()
            except PasswordError as err:
                print(str(err))
            else:
                entered_valid_pass = True

        if entered_valid_pass:
            self._database.change_pass(str(new_pass), self.logged_user)

    def _change_message(self):
        new_message = input("Enter your new message: ")
        self._database.change_message(new_message, self.logged_user)

    def _show_message(self):
        print(self.logged_user.get_message())

    def _help(self):
        print("info - for showing account info")
        print("changepass - for changing passowrd")
        print("change-message - for changing users message")
        print("show-message - for showing users message")
