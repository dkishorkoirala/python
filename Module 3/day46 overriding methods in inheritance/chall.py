class Vehicle:
    def start(self):
        print("Vehicle starting...")


class Bike(Vehicle):
    def start(self):
        print("Bike roaring to life!")


class Bus(Vehicle):
    def start(self):
        print("Bus engine starting...")


v = Vehicle()
v.start()

b = Bike()
b.start()

b = Bus()
b.start()
