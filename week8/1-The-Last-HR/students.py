import sqlite3


class Students:

    def __init__(self):
        self.db = sqlite3.connect('hackbulgaria.db')

    def insert(self, name, github, available):
        sql = "INSERT INTO students (name, github, available) VALUES (?, ?, ?)"
        cursor = self.db.cursor()
        cursor.execute(sql, (name, github, available))
        self.db.commit()
        inserted_id = cursor.lastrowid
        cursor.close()

        return inserted_id

    def assign_to_course(self, student_id, course_id, course_group):
        sql = "INSERT INTO student_courses (course_group, student_id, course_id) VALUES (?, ?, ?)"
        cursor = self.db.cursor()
        cursor.execute(sql, (course_group, student_id, course_id))
        self.db.commit()
        cursor.close()

    def get(self):
        sql = "SELECT id, name, github FROM students"
        cursor = self.db.cursor()
        cursor.execute(sql)
        get_students = cursor.fetchall()
        cursor.close()

        return get_students

    def get_students_and_courses(self):
        sql = "SELECT S.id AS student_id, S.name, S.github, SC.course_group, C.id as course_id, C.name as course_name FROM student_courses AS SC JOIN students as S JOIN courses AS C ON S.id == SC.student_id AND C.id == SC.course_id"

        cursor = self.db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()

        students_and_courses = {}
        for result in results:
            student_key = "%d - %s, %s" % (result[0], result[1], result[2])

            if student_key not in students_and_courses:
                students_and_courses[student_key] = []

            students_and_courses[student_key].append((result[3], result[4], result[5]))

        return students_and_courses
