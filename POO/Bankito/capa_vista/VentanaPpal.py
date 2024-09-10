from PySide6.QtWidgets import QApplication, QMainWindow
from capa_vista.ventanaPpal_ui import Ui_MainWindow
from capa_vista.ventanaNuevoCliente import *

# from formNuevoCliente import *
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #Conectar las acciones del MENU  a los metodos
        self.actionNuevo_Cliente.triggered.connect(self.nuevo_cliente)
        self.actionActualizar_Cliente.triggered.connect(self.actualizar_cliente)
        self.actionSALIR.triggered.connect(self.salir)

    def nuevo_cliente(self):
        # # Crear una instancia de la ventana "Nuevo Cliente"
        ventana = VentanaNuevoCliente()
        # Mostrar la ventana y esperar a que se cierre
        ventana.exec_()
    
    def actualizar_cliente(self):
        print("actualizar cliente")

    def salir(self):
        sys.exit()


        
#         #conectar menu con funcionalidad
#         self.actionNuevo_Cliente.triggered.connect(self.insertarNuevoCliente)
#         self.actionActualizar_Cliente.triggered.connect(self.actualizarCliente)
#         self.actionNuevo_Prestamo.triggered.connect(self.insertarNuevoPrestamo)
#         self.actionSALIR.triggered.connect(self.salir)
    
#     def insertarNuevoCliente(self):
#         # Crear una instancia de la ventana "Nuevo Cliente"
#         ventana = Ui_ventanaNuevoCliente()
#         # Mostrar la ventana y esperar a que se cierre
#         ventana.exec_()
    
#     def actualizarCliente(self):
#         print("actualizando cliente")
    
#     def insertarNuevoPrestamo(self):
#         print("insertando prestamo")

