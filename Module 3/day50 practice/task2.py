class Appliance:
    def turn_on(self):
        print("Turning on appliance...")


class Fan(Appliance):
    def turn_on(self):
        super().turn_on()
        print("Fan spinning...")


class SmartFan(Fan):
    def turn_on(self):
        super().turn_on()
        print("Voice control activated...")


smartfan = SmartFan()
smartfan.turn_on()
