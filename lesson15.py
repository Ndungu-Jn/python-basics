# Inheritance
# Error handling
# Dates
from datetime import datetime, date


class Employee:
    def __init__(self, name, id_number, date_of_birth, gender):
        self.name = name
        self.id_number = id_number
        self.date_of_birth = date_of_birth
        self.gender = gender
        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.age = date.today().year - date_of_birth.year

    def print_details(self):
        print(f"Name: {self.name}\nID: {self.id_number}\nDate: {self.date_of_birth}\nGender: {self.gender}\nAge: {self.age}")


class PermanentEmployee(Employee):
    def __init__(self, name, id_number, date_of_birth, gender, salary):
        super().__init__(name, id_number, date_of_birth, gender)
        self.salary = salary

    def print_salary(self):
        print(f"Salary: {self.salary}")

    #override
    def print_details(self):
        super().print_details()
        print(f"Salary is {self.salary}")



class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, date_of_birth, gender, hourly_pay, end_dates):
        super().__init__(name, id_number, date_of_birth, gender)
        self.hourly_pay = hourly_pay
        self.end_dates = end_dates

    def print_hourly_pay(self):
        print(f"Hourly pay: {self.hourly_pay}")

    def print_end_dates(self):
        print(f"End date: {self.end_dates}")


p1 = PermanentEmployee(salary=100000, name="Emma Muthaiga", id_number="67535278", gender="Female", date_of_birth="1990-01-26")
p1.print_details()
p1.print_salary()

t1 = TemporaryEmployee("John", id(35646783), date_of_birth="2000-3-15", gender="Male", hourly_pay=100000, end_dates="2020-3-15")
t1.print_details()

