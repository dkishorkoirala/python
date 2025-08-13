class Animal:
    def speak(self):
        print("Animal Sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")


class SmartDog(Dog):
    def speak(self):
        super().speak()
        print("Translating barks to human language ")


sd = SmartDog()
sd.speak()
