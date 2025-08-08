class Device:
    def boot(self):
        print("Booting Device...")


class Laptop(Device):
    def boot(self):
        super().boot()
        print("Laptop booted")


class GamingLaptop(Laptop):
    def boot(self):
        super().boot()
        print("Gaming Laptop booted")


l2 = GamingLaptop()
l2.boot()
