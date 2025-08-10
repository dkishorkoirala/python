class Appliance:
    def start(self):
        print("Starting Appliance...")


class WashingMachine(Appliance):
    def start(self):
        super().start()
        print("Washing Clothes...")


class SmartWashingMachine(WashingMachine):
    def start(self):
        super().start()
        print("Optimizing Wash Cycle...")


for w in [WashingMachine(), SmartWashingMachine()]:
    w.start()
