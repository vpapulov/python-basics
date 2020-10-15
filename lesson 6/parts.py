from dataclasses import dataclass

@dataclass
class CarEngine:
    volume: int
    number_of_valves: int
    max_rpm: int
    started: bool = False

    def start(self):
        self.started = True


@dataclass
class Bumper:
    width: int
