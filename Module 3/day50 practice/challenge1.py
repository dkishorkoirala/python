class Employee:
    def calculate_salary(self):
        print("Base salary calculated")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full-time salary calculated")


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part-time salary calculated")


class Contractor(Employee):
    def calculate_salary(self):
        super().calculate_salary()
        print("Contractor bonus added")


for e in [Employee(), FullTimeEmployee(), PartTimeEmployee(), Contractor()]:
    e.calculate_salary()
