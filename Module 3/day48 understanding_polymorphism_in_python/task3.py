class Device:
    def start(self):
        print("Device started...")


class Printer(Device):
    def start(self):
        print("Printer started...")


class Scanner(Device):
    def start(self):
        print("Scanner started...")


for dev in [Printer(), Scanner()]:
    dev.start()
