class Delivery:
    def deliver(self):
        print("Delivering package...")


class BikeDelivery(Delivery):
    def deliver(self):
        print("Delivering by bike")


class TruckDelivery(Delivery):
    def deliver(self):
        print("Delivering by truck")


class DroneDelivery(Delivery):
    def deliver(self):
        super().deliver()
        print("Flying drone to location")


for _ in [Delivery(), BikeDelivery(), TruckDelivery(), DroneDelivery()]:
    _.deliver()
