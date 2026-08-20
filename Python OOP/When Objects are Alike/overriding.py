class Vehicle:
    total_vehicles = 0

    def __init__(self, vin_number: str) -> None:
        self.vin_number = vin_number
        Vehicle.total_vehicles += 1


class ElectricCar(Vehicle):

    def __init__(self, vin_number: str, battery_power: str) -> None:
        super().__init__(vin_number)
        self.battery_power = battery_power


car1 = ElectricCar("EV123", "75 kWh")
car2 = ElectricCar("EV456", "100 kWh")

print(f"Car 1 Battery: {car1.battery_power}")
print(f"Total Fleet Count: {Vehicle.total_vehicles}")
