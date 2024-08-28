
from Vehiculos import *

class AutoElectrico(Vehiculos):
    def __init__(self, patente, marca, modelo):
        super().__init__(patente, marca, modelo)
        self.bateria=0  
        self.kmRecorridos=0
        #con carga al 100% autonomia de 200km / 50% 100km etc 

    def __str__(self):
        return super().__str__() + "con " + int(self.bateria) + "% de carga"

    def mostrarCarga(self):
        print(f'{self.bateria}%')
            
    def verificarCarga(self):
        print("Batery low" if self.bateria < 15 else "Batery OK")