# Definir una clase que represente la estructura de los datos en cada fila del CSV.
    # Clase Unidad y para guardar el tipo de unidad use un enumerado Tipo
# Leer el archivo CSV y, por cada fila, crear una instancia de esa clase.
# Guardar cada instancia en una lista.

from Unidad import *
import csv

class GestorUnidades():
    def __init__(self) -> None:
        self.lista_Unidades=[]

# Leer el archivo CSV y, por cada fila, crear una instancia de esa clase.
    def leer_Unidades(self):
        self.lista_Unidades=[]
        with open('./unidades.csv', mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                print(fila)
                unidad= Unidad(fila['IdUnidad'], fila['Identificacion'], fila['Descripcion'], fila['TipoUnidadId'])
                self.lista_Unidades.append(unidad)
                
        
    def imprimir_Unidades(self):
        for unidad in self.lista_Unidades:
            print(unidad)
    
    def imprimir_unidades_por_Tipo(self,tipo):
        for unidad in self.lista_Unidades:
            if unidad.esTipo(tipo):
                print(unidad) 

    def agregar_unidad(self,nuevaUnidad):
        self.lista_Unidades.append(nuevaUnidad)

    def borrar_Unidad(self,idunidad):
        for unidad in self.lista_Unidades:
            if unidad.esId(idunidad):
                self.lista_Unidades.remove(unidad)

    def guardar_Unidades(self):
        with open('./unidades.csv', mode='w', newline='',encoding='utf-8') as archivo:
            nombres_columnas = ['IdUnidad', 'Identificacion', 'Descripcion', 'TipoUnidadId']
            escritor_csv = csv.DictWriter(archivo, fieldnames=nombres_columnas)
            
            escritor_csv.writeheader()
            for unidad in self.lista_Unidades:
                escritor_csv.writerow({'IdUnidad': unidad.idUnidad,
                                    'Identificacion': unidad.identificacion,
                                    'Descripcion': unidad.descripcion,
                                    'TipoUnidadId':unidad.tipoUnidad})
            

####
gestor=GestorUnidades()
gestor.leer_Unidades()
gestor.imprimir_Unidades()

nueva=Unidad(118,"SSSS","SERVICIO SISTEMA SYS SIN",12)
gestor.agregar_unidad(nueva)

nueva=Unidad(119,"SSS1","SERVICIO SISTEMA SYS UNO",12)
gestor.agregar_unidad(nueva)

nueva=Unidad(120,"SSS2","SERVICIO SISTEMA SYS DOS",12)
gestor.agregar_unidad(nueva)

gestor.imprimir_Unidades()


gestor.guardar_Unidades()

gestor.borrar_Unidad(120)
gestor.imprimir_Unidades()


# gestor.leer_Unidades()
# gestor.imprimir_Unidades()

