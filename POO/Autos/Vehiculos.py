class Vehiculos():
    def __init__(self,patente,marca,modelo):
        self.patente=patente
        self.marca=marca
        self.modelo=modelo
        # enmarcha y estacionado se deben manejar juntos y opuestos
        self.__enMarcha=False
        self.__estacionado=True
        # puertas abiertas y kmxhora se maneja individuales (o mejor dicho son manejadas por un sensor)
        self.__kmxhora=0
        
    def __str__(self) :
        estado= "y esta en Marcha" if self.__enMarcha else "y esta parado" + f" a {self.__kmxhora} Km/hs "
        return f'{self.patente} - {self.marca} - {self.modelo} puertas ' + estado
    
    #comportamiento 
    def chequeo(self):
        return True if (not self.__enMarcha and self.__estacionado  and self.__kmxhora <= 0) else False
    
    def arrancar(self):
        if self.chequeo():
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
            print (f'el vehiculo {self.patente} acelero y ahora va a {self.__kmxhora} km/hora')
        else:
            print (f'el vehiculo {self.patente} continua a  {self.__kmxhora} km/hora porque no puede acelerar debido a que o esta una puerta abierta o esta estacionado o no esta en marcha')
        
    def stop(self):
        self.__enMarcha=False
        self.__estacionado=True

    def esta_circulando(self):
        return self.__enMarcha 
    
    def esta_estacionado(self):
        return self.__estacionado
    
    
     
    
