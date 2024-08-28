from Vehiculos import *

class Furgonetta(Vehiculos):

    def __init__(self, patente, marca, modelo):
        super().__init__(patente, marca, modelo)   # llamo a init del padre
        self.__cargada=0

    def chequeo(self): ## usando mismo nombre SOBREESCRIBO metodo del padre especializando
        return True if super().chequeo() and self.cargada >= 0 and self.cargada <= 1000  else False

    def esta_cargada(self):
        if self.cargado > 0 :
            return "La Furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
    
    def cargarFurfonetta(self,cargaenKilos):
        if self.chequeo():
            self.cargada += cargaenKilos
        else:
            print("no se puede cargar debido a problemas en los limites de carga")
    
    def descargarFurfonetta(self,cargaenKilos):
        if  self.chequeo() and self:
            self.cargada -= cargaenKilos
        else:
            print("no se puede descargar debido a problemas en los limites de carga")

