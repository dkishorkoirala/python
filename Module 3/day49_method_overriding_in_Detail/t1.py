class Appliance:
    def start(self):
        print("Appliance starting...")


class WashingMachine(Appliance):
    def start(self):
        print("Washing Machine starting...")


class MicroWave(Appliance):
    def start(self):
        print("MicroWave starting...")


a1 = Appliance()
a1.start()
print()

w1 = WashingMachine()
w1.start()
print()
m1 = MicroWave()
m1.start()
print()
