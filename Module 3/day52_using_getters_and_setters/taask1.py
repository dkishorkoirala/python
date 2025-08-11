class Marks:
    def __init__(self, mark):
        self.__mark = mark

    def get_mark(self):
        return f"Current marks: {self.__mark}"

    def set_mark(self, new_mark):
        if 0 <= new_mark <= 100:
            self.__mark = new_mark
            print("Marks updated successfully.")
        else:
            print("Marks must be between 0 and 100.")


m = Marks(85)
print(m.get_mark())
m.set_mark(90)
m.set_mark(900)
print(m.get_mark())
