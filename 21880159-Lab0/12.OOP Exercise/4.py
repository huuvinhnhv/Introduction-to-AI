# OOP Exercise 7: Check type of an object
# Write a program to determine which class a
# given Bus object belongs to.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def to_string(self):
        print("Car name: ", self.name)
        print("Max capacity: ", self.capacity)
        print("Mileage: ", self.mileage)


class Bus(Vehicle):
    pass


if __name__ == '__main__':
    bus_SG = Bus("So 51", 200, 50)
    bus_SG.to_string()
    print(type(bus_SG))
