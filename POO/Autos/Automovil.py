class Automovil():

    def __init__(self,color,puertas,patente) -> None:
        self.color=color
        self.puertas=puertas
        self.patente = patente
        self.__enMarcha=False
        self.__posPuertas= "cerradas"
        self.__kmxhora=0
        self.__estacionado=False
    
    def __str__(self) :
        enmarcha= "y esta en Marcha" if self.__enMarcha else "y esta parado"
        return f'{self.patente} - {self.color} - {self.puertas} puertas ' + enmarcha  

    
    #comportamiento
    def  parado(self):
        pass
    def circulando(self):
        pass
    def estacionado(self):
        pass
    def acelerar(self):
        pass
    def girar(self):
        pass
    def arrancar(self):
        pass



##################################
auto = Automovil("rojo",3,"AAA-111")
print(auto)
auto2 = Automovil("negro",5,"AAA-222")
print(auto2)