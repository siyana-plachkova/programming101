import sqlite3


def main():
    db = sqlite3.connect("hackbulgaria.db")

    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, github TEXT, available INTEGER)
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, name TEXT)
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_courses (
            id INTEGER PRIMARY KEY,
            course_group INTEGER,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
    """)
    db.commit()
    cursor.close()

    db.close()

if __name__ == '__main__':
    main()
