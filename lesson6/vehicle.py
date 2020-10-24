from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    name = ''
    mass = 0

    @abstractmethod
    def beep(self):
        raise NotImplemented
