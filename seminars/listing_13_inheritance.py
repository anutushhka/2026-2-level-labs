"""
Programming 2026.

Seminar 11.

Inheritance.
"""

# pylint:disable=too-few-public-methods


class Vehicle:
    """
    Represents a general vehicle.

    Instance attributes:
        max_speed (int): The maximum speed of the vehicle.
        colour (str): The colour of the vehicle.

    Instance methods:
        move() -> None:
            Simulates vehicle movement.
    """
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour
    def move(self):
        print(f"the {self.colour} vehicle moves at {self.max_speed}")
    def __str__(self):
        return f'Характеристики: макс.скорость {self.max_speed}, цвет {self.colour}'


class Car (Vehicle):
    """
    Represents a car, which is a type of vehicle.

    Instance attributes:
        max_speed (int): The maximum speed of the car.
        colour (str): The colour of the car.
        fuel (str): The type of fuel used by the car.

    Instance methods:
        move() -> None:
            Simulates car movement.
        stay() -> None:
            Simulates stopping the car.
    """
    def __init__(self, max_speed, colour, fuel):
        super().__init__(max_speed, colour)
        self.fuel = fuel
    def move(self):
        print(f"the {self.colour} car is moving at {max_speed} with {self.fuel} of fuel")
    def stay(self):
        print("The car has stopped")
    def __str__(self):
            return f'Характеристики: макс.скорость {self.max_speed}, цвет {self.colour}, топливо {self.fuel}'


class Bicycle (Vehicle):
    """
    Represents a bicycle, which is a type of vehicle.

    Instance attributes:
        number_of_wheels (int): The number of wheels of the bicycle.
        colour (str): The colour of the bicycle.
        max_speed (int): The maximum speed of the bicycle.

    Instance methods:
        move() -> None:
            Simulates bicycle movement.
        freestyle() -> None:
            Simulates performing a freestyle trick.
    """
    def __init__(self, number_of_wheels, colour, max_speed):
        super().__init__(max_speed, colour)
        self.number_of_wheels = number_of_wheels
    def move(self):
        print("the bicycle is moving")
    def freestyle(self):
        print("the bicycle is performing a fressstyke trick")
    def __str__(self):
        return f'Характеристики: макс.скорость {self.max_speed}, цвет {self.colour}, кол-во колёс {self.number_of_wheels}'


class Aircraft (Vehicle):
    """
    Represents an aircraft, which is a type of vehicle.

    Instance attributes:
        number_of_engines (int): The number of engines of the aircraft.
        colour (str): The colour of the aircraft.
        max_speed (int): The maximum speed of the aircraft.

    Instance methods:
        move() -> None:
            Simulates aircraft movement.
    """
    def __init__(self, number_of_engines, colour, max_speed):
        super().__init__(colour, max_speed)
        self.number_of_engines = number_of_engines
    def move(self):
        print("the aircraft moves")
    def __str__(self):
        return f'Характеристики: макс.скорость {self.max_speed}, цвет {self.colour}, крылья {self.number_of_engines}'


def main() -> None:
    """
    Launch listing.
    """
    print("Created inheritance hierarchy: Vehicle -> Car, Bicycle, Aircraft")
    car = Car(200, "красный", "дизель")
    b = Bicycle(10, "зелёный", 3)
    a = Aircraft(1000, "розовый", 3)

    print(car)
    print(b)
    print(a)



if __name__ == "__main__":
    main()
