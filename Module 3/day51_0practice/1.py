class SmartDevice:
    def activate(self):
        print("Activating Device...")


class SmartLight(SmartDevice):
    def activate(self):
        print("Activating Light...")


class SmartSpeaker(SmartDevice):
    def activate(self):
        print("Activating speaker...")


for m in [SmartLight(), SmartSpeaker()]:
    m.activate()
