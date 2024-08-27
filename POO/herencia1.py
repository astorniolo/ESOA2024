
class ClasePadre:
    def printHola(self):
        print('Hola, mundo! soy Papa')

class ClaseHijo(ClasePadre):
    def unMetDeHIjo(self):
        print("La clase padre no tiene este metodo es especificidad del HIJO!!!! soy primer HIJO de papa")

class ClaseHermano(ClasePadre):
    def unMetDeHermano(self):
        print("un metodo del hemarno o segundo hijo del Padre solo el hermano lo puede ejecutar!!!!!! soy segundo hijo de papa!!! el hermnano soltero")

class ClaseNieto(ClaseHijo):
    def unMetDeMieto(self):
        print('Solo el NIETO puede ver este metodo es especificidad del NIETO!!! soy Nieto')


#############MAIN
print('Crear un OBJ de la clase PADRE y llamar a sus metodos')
padre = ClasePadre()
padre.printHola()

print('Crear un OBJ de la clase HIJO y llamar a sus metodos propio y heredados')
hijo= ClaseHijo()
#propio
hijo.unMetDeHIjo()
#heredado
hijo.printHola()


print('Crear un OBJ de la clase NIETO y llamar a sus metodos propio y heredados')
nieto = ClaseNieto()
#propio
nieto.unMetDeMieto()
#heredado
nieto.unMetDeHIjo()
nieto.printHola()


print(' error:')
padre.unMetDeMieto()

Hermano=ClaseHermano()
Hermano.unMetDeHermano()
Hermano.printHola()