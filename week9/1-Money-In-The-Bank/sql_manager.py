import sqlite3
from client import Client


class Database:

    def __init__(self):
        self._conn = sqlite3.connect("bank.db")
        self._cursor = self._conn.cursor()

    @property
    def conn(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def create_clients_table(self):
        create_query = '''CREATE TABLE IF NOT EXISTS
            clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    email TEXT,
                    password TEXT,
                    balance REAL DEFAULT 0,
                    message TEXT,
                    reset_password_hash TEXT)'''

        self._cursor.execute(create_query)

    def change_message(self, new_message, logged_user):
        update_sql = "UPDATE clients SET message = ? WHERE id = ?"

        self._cursor.execute(update_sql, (new_message, logged_user.get_id()))
        self._conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        update_sql = "UPDATE clients SET password = ? WHERE id = ?"

        self._cursor.execute(update_sql, (new_pass, logged_user.get_id()))
        self._conn.commit()

    def register(self, username, email, password):
        insert_sql = "INSERT INTO clients (username, email, password) VALUES (?, ?, ?)"

        self._cursor.execute(insert_sql, (username, email, password))
        self._conn.commit()

    def login(self, username, password):
        select_query = "SELECT id, username, balance, message, email FROM clients WHERE username = ? AND password = ? LIMIT 1"

        self._cursor.execute(select_query, (username, password))
        user = self._cursor.fetchone()

        if user:
            return Client(user[0], user[1], user[2], user[3], user[4])
        else:
            return False

    def get_user_email(self, username):
        get_email = "SELECT email FROM clients WHERE username = ? LIMIT 1"

        self._cursor.execute(get_email, (username, ))
        user = self._cursor.fetchone()

        if user:
            return user[0]

        return False

    def update_reset_pass(self, reset_pass_hash, username):
        update_reset_pass_hash = "UPDATE clients SET reset_password_hash = ? WHERE username = ?"

        self._cursor.execute(update_reset_pass_hash, (reset_pass_hash, username))
        self._conn.commit()

    def close(self):
        self._cursor.close()
        self._conn.close()
