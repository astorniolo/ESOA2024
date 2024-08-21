class Perro:
    # Atributo de Clase
    genero= "Canis"
    
    def __init__(self, nombre, edad, raza, color):

        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color

    # Métodos de instancia
    def imprimir(self):
        return f'{self.nombre} es un {self.raza} {self.color} y tiene {self.edad} años.'
    
    def comer(self, comida):
        print( f'{self.nombre} esta comiendo {comida}.')

    def ladrar(self):
        return f'{self.nombre} dice  Guau Guau!.'

    # # Se puede reemplazar el método imprimir() con __str__()
    # def __str__(self):
    #     return f'{self.nombre} es un {self.raza} {self.color} y tiene {self.edad} años.'

miMascota = Perro("Renata", 9, "coker","te con leche")
print(miMascota)
print("observar que imprimieo la direccion Heap del OBJETO")

print("en la funcion impromir se retorna un string si no o recibo o no hago nada no pasa nada")
miMascota.imprimir()
print("que susece ahora")
print(miMascota.imprimir())
impresion=miMascota.imprimir()
print(impresion)

print("python nops ofrece una funcion para pasr a string mi objeto que obviamente tengo que definir yo")
print("Ahora probar imprimir mascota luego de definir __str__")
print(miMascota)

print("utilizaciond de los metodos")
print(miMascota.ladrar())
miMascota.comer("purina")

print("Género:", miMascota.genero)
print(miMascota.imprimir())
print(miMascota.ladrar())
print(miMascota)
