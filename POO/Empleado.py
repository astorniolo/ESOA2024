class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado: ")
        self.sueldo=float(input("Ingrese el sueldo: "))

    def __del__(self):
        print('Método delete llamado')

    def imprimir(self):
         print("Nombre: {}".format(self.nombre))
         print("Sueldo: {}".format(self.sueldo))
        #  print("Nombre: {} - Sueldo {}".format(self.nombre, self.sueldo))

    def paga_impuestos(self):
        if self.sueldo>700000:
            print("Debe pagar impuestos a las ganancias")
        else:
            print("No paga impuestos  a las ganancias")


# Bloque Principal
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()