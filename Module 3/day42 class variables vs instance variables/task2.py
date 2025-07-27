class Student:
    count = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1


print(Student.count)
s1 = Student("Ram", 10)
print(s1.name, s1.grade, s1.count)
s2 = Student("Hari", 11)
print(s2.name, s2.grade, s2.count)
s3 = Student("Sita", 12)
print(s3.name, s3.grade, s3.count)
# print(s3.count)
print(Student.count)
