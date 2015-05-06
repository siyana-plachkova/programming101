import sqlite3


class Company:

    def __init__(self):
        self.db = sqlite3.connect("company.db")

    def get_employee(self, employee_id):
        sql = "SELECT * FROM users WHERE id=?"
        cursor = self.db.cursor()
        cursor.execute(sql, (employee_id,))
        user = cursor.fetchone()
        cursor.close()

        return user

    def get_employees(self):
        sql = "SELECT id, name, position FROM users"
        cursor = self.db.cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        cursor.close()

        return all_rows

    def get_monthly_spending(self):
        sql = "SELECT monthly_salary FROM users"
        cursor = self.db.cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        cursor.close()

        return sum([row[0] for row in all_rows])

    def get_yearly_spending(self):
        yearly_spending = self.get_monthly_spending() * 12

        sql = "SELECT yearly_bonus FROM users"
        cursor = self.db.cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        cursor.close()

        yearly_spending += sum([row[0] for row in all_rows])
        return yearly_spending

    def add_employee(self, employee_data):
        sql = "INSERT INTO users (name, monthly_salary, yearly_bonus, position) VALUES(?, ?, ?, ?)"

        cursor = self.db.cursor()
        cursor.execute(sql, employee_data)
        self.db.commit()
        cursor.close()

    def delete_employee(self, employee_id):
        employee = self.get_employee(employee_id)

        sql = "DELETE FROM users WHERE id=?"
        cursor = self.db.cursor()
        cursor.execute(sql, (employee_id, ))
        self.db.commit()
        cursor.close()

        return employee

    def update_employee(self, employee_id, employee_data):
        employee_data = list(employee_data)
        employee_data.append(employee_id)
        sql = "UPDATE users SET name=?, monthly_salary=?, yearly_bonus=?, position=? WHERE id=?"

        cursor = self.db.cursor()
        cursor.execute(sql, tuple(employee_data))
        self.db.commit()
        cursor.close()


class ManageCompany:

    def __init__(self):
        self.company = Company()

    def start(self):
        while True:
            command = input("command>")

            if command == "list_employees":
                self._list_employees()
            elif command == "monthly_spending":
                self._monthly_spending()
            elif command == "yearly_spending":
                self._yearly_spending()
            elif command == "add_employee":
                self._add_employee()
            else:
                command_split = command.split(' ')

                if len(command_split) == 2:
                    command = command_split[0]
                    employee_id = int(command_split[1])

                    if command == "delete_employee":
                        self._delete_employee(employee_id)
                    elif command == "update_employee":
                        self._update_employee(employee_id)

    def _list_employees(self):
        for row in self.company.get_employees():
            print("%d - %s - %s" % row)

    def _monthly_spending(self):
        print("The company is spending $%d every month!" % self.company.get_monthly_spending())

    def _yearly_spending(self):
        print("The company is spending $%d every year!" % self.company.get_yearly_spending())

    def _add_employee(self):
        self.company.add_employee(self._get_employee_input())

    def _delete_employee(self, employee_id):
        deleted_user = self.company.delete_employee(employee_id)

        print("%s was deleted." % deleted_user[1])

    def _update_employee(self, employee_id):
        self.company.update_employee(employee_id, self._get_employee_input())

    def _get_employee_input(self):
        name = input("name>")
        monthly_salary = input("monthly_salary>")
        yearly_bonus = input("yearly_bonus>")
        position = input("position>")

        return (name, int(monthly_salary), int(yearly_bonus), position)


if __name__ == '__main__':
    company = ManageCompany()
    company.start()
