class Public_Private:
    def __init__(self, private):
        self.__private = private

    def display(self):
        print(f"Accessed private attribute: {self.__private}")


pp = Public_Private("I am private")
pp.display()
