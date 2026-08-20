from abc import ABC, abstractmethod  # used to make a class 'abstract'


# Important use of 'ABC' to define an abstract class
class Vehicle(ABC):
    def start_engine(self): ...  # Here, 'pass' keyword can also be used

    def honk(self) -> str:
        return "Beep Beep!"


# Implement a concrete subclass
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started!"


# Implement another concrete subclass
class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started!"


my_car = Car()
my_truck = Truck()

print(my_car.start_engine())
print(my_truck.start_engine())

print(my_car.honk())
