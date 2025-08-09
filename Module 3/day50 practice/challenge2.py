class Transport:
    def book(self):
        print("Booking transport...")


class Bus(Transport):
    def book(self):
        print("Booking a bus ticket...")


class Train(Transport):
    def book(self):
        print("Booking a train ticket...")


class Flight(Transport):
    def book(self):
        super().book()
        print("Booking in-flight meals...")


for tickets in [Bus(), Train(), Flight()]:
    tickets.book()
