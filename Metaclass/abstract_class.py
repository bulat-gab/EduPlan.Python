from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def refill_tank(self, litres):
        pass

    @abstractmethod
    def move_ahead(self):
        pass

class Truck(Vehicle):
    def __init__(self, company, color, wheels):
        self.company = company
        self.color = color
        self.wheels = wheels

    def refill_tank(self, litres):
        print('Refilled')

    def move_ahead(self):
        print('Moved')

t = Truck('Tesla', 'Black', 4)
