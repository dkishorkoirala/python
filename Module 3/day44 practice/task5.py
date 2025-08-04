class Student:
    max_students = 3
    current_count = 0

    def __init__(self, name):
        if Student.current_count >= Student.max_students:
            print("cannot add more students")

        else:
            self.name = name
            Student.current_count += 1
            print(f"Student created successfully {self.name}")


s1 = Student("A")
s2 = Student("B")
s3 = Student("C")
s4 = Student("D")
s5 = Student("E")
