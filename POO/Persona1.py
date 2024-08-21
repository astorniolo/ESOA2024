class Persona():
    #variables de clase 
    _tienelunares=False
    __tienepecas=False 
    tienecanas=False

#Constructor
    def __init__(self, nombre, apellido,trabaja, edad) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self._trabaja=trabaja
        self.__edad=edad

#Metodos
#Metodos de consulta
    def edad(self):         # OJO no olvidarse nunca Nunca NUNCA el self como parametro en cada metodo
        return self.__edad
    
    def imprimir(self):
        return f' {self.apellido.upper()}, {self.nombre.capitalize()} tiene {self.edad()} años'


#################### MAIN
andrea=Persona("andrea","dosantos",True,37)
print(andrea)
print(andrea.imprimir())
print(andrea.apellido)
#print(andrea.__edad)
print(andrea.edad())
#print(andrea.__tienepecas)
print(andrea._tienelunares)
print(andrea.tienecanas)
#andrea.__tienepecas=True
andrea._tienelunares=True
andrea.tienecanas=True
#print(andrea.__tienepecas)
print(andrea._tienelunares)
print(andrea.tienecanas)