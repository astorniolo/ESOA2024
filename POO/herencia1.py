class ClasePadre:
    def printHola(self):
        print('Hola, mundo!')

class ClaseHijo(ClasePadre):
    def unMetodoNuevoDelHIJO(self):
        print("La clase padre no tiene este metodo")

class ClaseNieto(ClaseHijo):
    def unMetodoNuevodeNIETO(self):
        print('Solo el NIETO puede ver este metodo')

#############MAIN
print('Crear un OBJ de la clase PADRE y llamar a sus metodos')
padre = ClasePadre()
padre.printHola()

print('Crear un OBJ de la clase HIJO y llamar a sus metodos propio y heredados')
hijo= ClaseHijo()
#propio
hijo.unMetodoNuevoDelHIJO()
#heredado
hijo.printHola()


print('Crear un OBJ de la clase NIETO y llamar a sus metodos propio y heredados')
nieto = ClaseNieto()
nieto.unMetodoNuevodeNIETO()
nieto.unMetodoNuevoDelHIJO()
nieto.printHola()


print(' error:')
padre.unMetodoNuevodeNIETO()