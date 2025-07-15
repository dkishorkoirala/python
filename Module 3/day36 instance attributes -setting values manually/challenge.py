class Student:
    def introduce(self):
        print("Hi, I'm " + self.name + ". I'm " + self.age + " years old and in grade " + self.grade + ".")


s1 = Student()
s2 = Student()

s1.name = "Hari"
s2.name = "Ram"

s1.age = "20"
s2.age = "21"

s1.grade = "A"
s2.grade = "B"

s1.introduce()
s2.introduce()