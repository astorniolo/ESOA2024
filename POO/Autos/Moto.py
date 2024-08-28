
from Vehiculos import *

class Moto(Vehiculos):
    def __init__(self, patente, marca, modelo):
        super().__init__(patente, marca, modelo)
        self.haceWilly = "no hago willy"

    def __str__(self):
        return super().__str__() + self.haceWilly

    def Willy(self):
        self.haceWilly="voy haciendo Willy"

    def stopWilly(self):
        self.haceWilly="no hago willy"