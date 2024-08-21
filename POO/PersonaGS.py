class Persona: #Creamos la clase (class + sustantivo en singular en mayúscula)
    #variables de clase 
    _tienelunares=False
    __tienepecas=False
    tienecanas=False

#Constructor
    def __init__(self, nombre, apellido, edad) -> None:
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad

#Getters y Setters
    # getter y setter para el atributo privado nombre
    # El orden es importante: 1ro el getter y luego el setter
    @property
    def nombre(self):
        return self.__nombre #Obtiene el nomnbre
    
    @nombre.setter
    def nombre(self, nombre): #Repetimos el nombre del método y en el decorador
        self.__nombre= nombre #Es el nombre que le paso como parámetro a la función
    
    @property
    def apellido(self):
        return self.__apellido 
    
    @nombre.setter
    def nombre(self, apellido): 
        self.__apellido= apellido

    @property
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def edad(self, edad): 
        self.__edad= edad

#Comportamiento
    def __str__(self) -> str:
        return "{}, {} : {} años ".format(self.apellido,self.nombre, self.edad)
    
    def imprimirNombre(self): #Método para mostrar datos
        print("Nombre: {}".format(self.nombre))
    
    def cumplirAños(self):
        self.edad+=1
        

# Programa principal
andrea=Persona("Andrea","Storniolo",55) #Creamos un objeto
print(andrea)
andrea.nombre="Andreita"
print(andrea)
