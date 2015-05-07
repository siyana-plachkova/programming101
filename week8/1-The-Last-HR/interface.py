from students import Students
from courses import Courses


class Interface:

    def __init__(self):
        self.students = Students()
        self.courses = Courses()

    def start(self):
        while True:
            command = input("command: ")

            if command == "list_students":
                self._list_students()
            elif command == "list_courses":
                self._list_courses()
            elif command == "list_students_and_courses":
                self._list_students_and_courses()
            elif command == "list_students_with_most_courses":
                self._list_students_with_most_courses()

    def _list_students(self):
        for student in self.students.get():
            print("%d - %s, %s" % student)

    def _list_courses(self):
        for course in self.courses.get():
            print("%d - %s" % course)

    def _list_students_and_courses(self):
        students_and_courses = self.students.get_students_and_courses()

        for student in students_and_courses.keys():
            print("%s, courses:" % student)
            for course in students_and_courses[student]:
                print("     course: %s, group: %d" % (course[2], course[1]))

    def _list_students_with_most_courses(self):
        students_and_courses = self.students.get_students_and_courses()
        most_courses = max([len(value) for value in students_and_courses.values()])

        for student in students_and_courses:
            if most_courses == len(students_and_courses[student]):
                print("%s, courses:" % student)
                for course in students_and_courses[student]:
                    print("     course: %s, group: %d" % (course[2], course[1]))

if __name__ == '__main__':
    interface = Interface()
    interface.start()
