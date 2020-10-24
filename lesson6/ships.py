from vehicle import Vehicle


class Ship(Vehicle):
    def __init__(self, name, mass, displacement):
        self.name = name
        self.mass = mass
        self.displacement = displacement

    def __repr__(self):
        return 'ship ' + self.name

    def beep(self):
        print("faaaaaam")


class Sailboat(Ship):
    def __init__(self, name, mass, displacement):
        super().__init__(name, mass, displacement)

    def __repr__(self):
        return 'sailboat ' + self.name
