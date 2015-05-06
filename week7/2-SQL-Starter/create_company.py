import sqlite3


class CreateCompany:

    def __init__(self):
        self.db = sqlite3.connect('company.db')

        cursor = self.db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)")
        self.db.commit()
        cursor.close()

    def fill_data(self):
        cursor = self.db.cursor()
        users = [("Ivan Ivanov", 5000, 10000, "Software Developer"),
                 ("Rado Rado", 500, 0, "Technical Support Intern"),
                 ("Ivo Ivo", 10000, 100000, "CEO"),
                 ("Petar Petrov", 3000, 1000, "Marketing Manager"),
                 ("Maria Georgieva", 8000, 10000, "COO")]
        cursor.executemany("INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?, ?, ?, ?)", users)
        self.db.commit()
        cursor.close()

if __name__ == '__main__':
    company = CreateCompany()
    company.fill_data()
