
class Vehicle:
    def __init__(self, registration, odometer, fuel):
        self.registration = registration
        self.odometer = odometer
        self.fuel = fuel

    def __calc_remaining_km(self):
        print("calc")

    def get_fuel_left(self):
        return self.fuel

    def honk(self):
        print("Toot!")
        self.__calc_remaining_km()

    def __setitem__(self, key, value):

class Car(Vehicle):
    def honk(self):
        print("Hooonk!")

volkswagen = Car("AB123", 112000, 24.3)
print(volkswagen.get_fuel_left()) # --> 24.3
volkswagen.honk() # --> Hooonk!

