import sqlite3


class Courses:

    def __init__(self):
        self.db = sqlite3.connect('hackbulgaria.db')

    def insert(self, name):
        course = self.get_by_name(name)

        if not course:
            sql = "INSERT INTO courses (name) VALUES (?)"

            cursor = self.db.cursor()
            cursor.execute(sql, (name, ))
            self.db.commit()
            inserted_id = cursor.lastrowid
            cursor.close()
            return inserted_id
        else:
            return course[0]

    def get(self):
        sql = "SELECT * FROM courses"

        cursor = self.db.cursor()
        cursor.execute(sql)

        courses = cursor.fetchall()

        cursor.close()

        return courses

    def get_by_name(self, name):
        sql = "SELECT * FROM courses WHERE name = ?"

        cursor = self.db.cursor()
        cursor.execute(sql, (name, ))

        course = cursor.fetchone()

        cursor.close()

        return course
