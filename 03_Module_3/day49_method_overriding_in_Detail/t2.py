class Vehicle:
    def start_engine(self):
        print("Starting engine...")


class Car(Vehicle):
    def start_engine(self):
        super().start_engine()
        print()
        print("Driving off!")


c1 = Car()
c1.start_engine()
