# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class
# with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def to_string(self):
        print("Car name: ", self.name)
        print("Max speed: ", self.max_speed)
        print("Mileage: ", self.mileage)


class Bus(Vehicle):
    pass


if __name__ == '__main__':
    bus_SG = Bus("So 51", 200, 12)
    bus_SG.to_string()
