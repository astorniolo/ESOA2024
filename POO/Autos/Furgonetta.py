from Vehiculos import *

class Furgonetta(Vehiculos):

    def __init__(self, patente, marca, modelo):
        super().__init__(patente, marca, modelo)   # llamo a init del padre
        self.__carga=0

    def chequeo(self): ## usando mismo nombre SOBREESCRIBO metodo del padre especializando
        return super().chequeo() and self.__carga >= 0 and self.__carga <= 1000  
    
    def esta_cargada(self):
        if self.cargado > 0 :
            return "La Furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
    
    def cargarFurgoneta(self,cargaenKilos):
        if self.chequeo() and (1000-self.__carga) >= cargaenKilos:
            self.__carga += cargaenKilos
        else:
            print(f"Problemas en los limites de carga. Actual {self.__carga} kilo Maximo a cargar {1000-self.__carga} kilos  ")
    
    def descargarFurgoneta(self,cargaenKilos):
        if  self.chequeo() and self.__carga >= cargaenKilos:
            self.__carga -= cargaenKilos
        else:
            print("Problemas en los limites de carga, solo puede descargar ",self.__carga)

#main
furgon=Furgonetta("AB123CD","peugeot","partner")
print(furgon)
# metodos heredados
furgon.arrancar()
furgon.acelerar()
furgon.acelerar()
furgon.acelerar()
furgon.acelerar()
furgon.stop()
if furgon.esta_estacionado() :
    print("esta estacionado")
#propios
furgon.cargarFurgoneta(300)
furgon.descargarFurgoneta(400)
print(furgon)
furgon.descargarFurgoneta(200)
print(furgon)