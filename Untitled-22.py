class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return 250

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return 340


def display_specs(car):
    """
    Demonstrates polymorphism:
    Regardless of the car’s actual class, as long as it implements
    fuel_type() and max_speed(), this function will work.
    """
    print(f"Fuel Type : {car.fuel_type()}")
    print(f"Max Speed : {car.max_speed()} km/h")

def main():

    cars = [BMW(), Ferrari()]

    for car in cars:


        print(f"{car.__class__.__name__} Specs:")
        display_specs(car)
        print("-" * 30)

if __name__ == "__main__":
    main()
