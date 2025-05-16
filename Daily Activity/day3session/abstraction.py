from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Bike(Vehicle):
    def fuel_type(self):
        print("Bike uses petrol.")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Electric Car Uses Battery")

b = Bike()
e = ElectricCar()

e.fuel_type()
b.fuel_type()