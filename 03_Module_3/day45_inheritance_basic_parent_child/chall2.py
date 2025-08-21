class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_id(self):
        print(f"Employee ID: {self.employee_id}")


e1 = Employee("Kiran", 25, 1)
e1.introduce()
e1.show_id()
