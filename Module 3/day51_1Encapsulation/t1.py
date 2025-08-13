class Public_Private:
    def __init__(self, public, private):
        self.public = public
        self.__private = private

    def display(self):
        print(f"Public attribute: {self.public}")
        try:
            print(f"Private attribute: {self.private}")
        except AttributeError:
            print("Cannot access private attribute directly: AttributeError")


pp = Public_Private("I am visible", "I am private")
pp.display()
