class employee:
    total_employee = 0

    def __init__(self, name):
        self.name = name
        employee.total_employee += 1


e1 = employee("Kiran")
e2 = employee("Sita")
e3 = employee("Hari")
print(employee.total_employee)
