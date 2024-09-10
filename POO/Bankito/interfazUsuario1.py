from PySide6.QtWidgets import QApplication, QMainWindow
from capa_Vista.ventanappal6_ui import Ui_MainWindow
from formNuevoCliente import *
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #Conectar las acciones a los metodos
        self.actionnuevo.triggered.connect(self.nuevo_cliente)
        self.actionactualizar.triggered.connect(self.actualizar_cliente)
        self.actionSALIR.triggered.connect(self.salir)

    def nuevo_cliente(self):
        # Crear una instancia de la ventana "Nuevo Cliente"
        ventana = VentanaNuevoCliente()
        # Mostrar la ventana y esperar a que se cierre
        ventana.exec_()
    
    def actualizar_cliente(self):
        print("actualizar cliente")

    def salir(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
