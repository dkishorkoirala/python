class Vehicle:
    def move(self):
        print("Moving...")


class Car(Vehicle):
    def move(self):
        print("Car is driving...")


car1 = Car()
car1.move()
