class Automovil():

    def __init__(self,color,puertas,patente) -> None:
        self.color=color
        self.puertas=puertas
        self.patente = patente
        # enmarcha y estacionado se deben manejar juntos y opuestos
        self.__enMarcha=False
        self.__estacionado=True
        # puertas abiertas y kmxhora se maneja individuales (o mejor dicho son manejadas por un sensor)
        self.__puertasAbiertas= False
        self.__kmxhora=0
    
    
    def __str__(self) :
        enmarcha= "y esta en Marcha" if self.__enMarcha else "y esta parado"
        return f'{self.patente} - {self.color} - {self.puertas} puertas ' + enmarcha
    
    #comportamiento 
    def chequeoPreArranque(self):
        return True if (not self.__enMarcha and self.__estacionado and not self.__puertasAbiertas  and self.__kmxhora <= 0) else False
    
    def arrancar(self):
        if self.chequeoPreArranque():
            self.__enMarcha=True
            self.__estacionado=False
            self.__kmxhora=10
            print(self,"arranco a 10 km/hora")
        else:
            self.__enMarcha=False
            print("por problemas internos no se puede poner el auto en marcha")

    def acelerar(self):
        if (self.__enMarcha and not self.__estacionado and not self.__puertasAbiertas):
            self.__kmxhora += 10
            print (f'el auto acelero y ahora va a {self.__kmxhora} km/hora')
        else:
            print (f'el continua a  {self.__kmxhora} km/hora porque no puede acelerar debido a que o esta una puerta abierta o esta estacionado o no esta en marcha')
        
    def stop(self):
        self.__enMarcha=False
        self.__estacionado=True

    def esta_circulando(self):
        return self.__enMarcha 
    
    def esta_estacionado(self):
        return self.__estacionado
    
   


##################################
auto = Automovil("rojo",3,"AAA-111")
print(auto)
auto2 = Automovil("negro",5,"AAA-222")
print(auto2)
auto.arrancar()
auto.acelerar()
auto.acelerar()
auto.acelerar()
auto.acelerar()
auto.acelerar()
print(auto.esta_circulando())
print(auto.esta_estacionado())
auto.stop()
print(auto)
print(auto.esta_circulando())
print(auto.esta_estacionado())