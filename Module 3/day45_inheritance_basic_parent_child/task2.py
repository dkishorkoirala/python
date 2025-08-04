class Vehicle:
    def start(self):
        print("Vehicle starting...")


class Car(Vehicle):
    def drive(self):
        print("Car driving...")


c = Car()
c.start()
c.drive()
