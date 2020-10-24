from vehicle import Vehicle
from exceptions import LightsAlreadyOnError


class Car(Vehicle):
    WHEEL_COUNT = 4

    def __init__(self, name, mass, fuel_consumption):
        self.name = name
        self.mass = mass
        if fuel_consumption <= 0:
            raise ValueError('fuel consumption must be positive')
        self.fuel_consumption = fuel_consumption
        self.lights_on = False
        self.fuel = 0
        self.engine = None
        self.bumper = None

    def __repr__(self):
        return 'car ' + self.name

    def beep(self):
        print("beep-beep")

    def turn_lights_on(self):
        if self.lights_on:
            raise LightsAlreadyOnError
        self.lights_on = True

    def turn_lights_off(self):
        self.lights_on = False

    def fill_up(self, litres):
        self.fuel += litres

    def can_drive_for_distance(self, kms):
        return self.fuel > kms / 100 * self.fuel_consumption


class Passenger_Car(Car):
    def __init__(self, name, mass, fuel_consumption):
        super().__init__(name, mass, fuel_consumption)

    def __repr__(self):
        return 'passenger car ' + self.name
