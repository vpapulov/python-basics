from vehicle import Vehicle


class Airplane(Vehicle):
    WHEEL_COUNT = 6

    def __init__(self, name, mass, max_height):
        self.name = name
        self.mass = mass
        self.max_height = max_height

    def __repr__(self):
        return 'airplane ' + self.name

    def beep(self):
        print("no sound")
