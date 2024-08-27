from Tipo import *

class Unidad:
    
    def __init__(self,IdUnidad,Identificacion,Descripcion,TipoUnidadId) -> None:
        self.idUnidad=IdUnidad
        self.identificacion=Identificacion
        self.descripcion=Descripcion
        self.tipoUnidad=TipoUnidadId
               

    def __str__(self) -> str:
        #return f'Id={self.idUnidad} - Identificacion={self.identificacion} - Descripcion={self.descripcion} -"tipo {self.tipoUnidad} - {Tipo(self.tipoUnidad)}'
        return f'Id={self.idUnidad} - Identificacion={self.identificacion} - Descripcion={self.descripcion} - {self.tipoUnidad}'
    
    def esTipo(self,tipo):
        return True if self.tipoUnidad==tipo else False
    
    def esId(self,id):
        return True if self.idUnidad==id else False

# ##########
# u=Unidad(73,"CBSP","CORBETA ARA SPIRO",3)
# print(u)
