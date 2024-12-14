from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def honk(self):
        pass

class Car(Vehicle):
    def honk(self):
        print("Hooonk!")

class Motorcycle(Vehicle):
    def honk(self):
        print("HUNK!")

volkswagen = Car()
yamaha = Motorcycle()
saab = Car()
harley = Motorcycle()

vehicles = [volkswagen, yamaha, saab, harley]

for vehicle in vehicles:
    vehicle.honk() # --> Hooonk! HUNK! Hooonk! HUNK!