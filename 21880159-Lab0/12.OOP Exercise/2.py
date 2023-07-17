# OOP Exercise 4: Class Inheritance
# Given:
# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a
# default value of 50.
# Use the following code for your parent Vehicle class.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def to_string(self):
        print("Car name: ", self.name)
        print("Max speed: ", self.max_speed)
        print("Mileage: ", self.mileage)


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


if __name__ == '__main__':
    bus_SG = Bus("So 51", 200, 12)
    bus_SG.to_string()
    print(bus_SG.seating_capacity())
