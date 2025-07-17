class Light:
    def switch_on(self):
        print(f"{self.brand} light of {self.wattage} watt is ON")


l = Light()
l.brand = "Philips"
l.wattage = 10

l.switch_on()