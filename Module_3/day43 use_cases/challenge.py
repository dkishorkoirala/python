class Students:
    max_students = 3
    current_count = 0

    def __init__(self, name, grade):
        if Students.current_count >= Students.max_students:
            print("cannot add more students")
            return

        self.name = name
        self.grade = grade
        Students.current_count += 1
        print(f"{self.name} of grade {self.grade} is added successfully")


s1 = Students("Ram", 10)
s2 = Students("Sita", 9)
s3 = Students("Hari", 8)
s4 = Students("Gita", 5)
