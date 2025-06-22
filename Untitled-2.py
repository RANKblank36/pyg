class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 200


class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_fee = 0.10 * base_fare
        total_fare = base_fare + maintenance_fee
        return total_fare


my_bus = Bus(50)
print(f"Total Bus Fare: INR {my_bus.fare():.0f}")
