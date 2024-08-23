from Punto import *

#Semantica por referencia
punto1=Punto(10,-30)
print(punto1)
punto1.imprimir_cuadrante()

punto2=Punto(3,6)
punto3=Punto(3,6)
print("son iguales" if (punto2==punto3) else "no son iguales")

if punto2.coordenadasIguales(punto3) :
    print(f"{punto2} y {punto3} tienen las mismas coordenadas")
else:
    print("tienen coordenadas diferentes")

punto3=punto2
print("son iguales" if (punto1==punto2) else "no son iguales")