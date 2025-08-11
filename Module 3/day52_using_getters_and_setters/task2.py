class Marks:
    def __init__(self, mark):
        self.__mark = mark

    @property
    def mark(self):
        return f"Current marks: {self.__mark}"

    @mark.setter
    def mark(self, new_mark):
        if 0 <= new_mark <= 100:
            self.__mark = new_mark
            print("Marks updated successfully.")
        else:
            print("Marks must be between 0 and 100.")


m = Marks(85)
print(m.mark)
m.mark = 90
m.mark = 1100
print(m.mark)
