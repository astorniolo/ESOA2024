import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from capa_vista.ventanaNuevoCliente_ui import Ui_ventanaNuevoCliente
from PySide6.QtWidgets import QDialog, QMessageBox
from capa_Negocio.ClienteDB import *

class VentanaNuevoCliente(QDialog, Ui_ventanaNuevoCliente):
    def __init__(self):
        super(VentanaNuevoCliente, self).__init__()
        self.setupUi(self)

        # Conectar el botón "Agregar Cliente" con su función
        self.btnGuardar.clicked.connect(self.agregar_cliente)
        self.btnCancelar.clicked.connect(self.close)

    def agregar_cliente(self):
        # Obtener el texto de los campos de texto
        nombre = self.txtNombre.text()
        domicilio = self.txtDomicilio.text()

        # Validar que los campos no estén vacíos
        if nombre and domicilio:
            # Aquí podrías agregar el cliente a una base de datos o realizar alguna otra acción
            cliente=ClientDB()
            id=cliente.proximoId()
            cliente.crear_nuevo(id, nombre, domicilio)

            print(f"Cliente agregado:{id} {nombre}, {domicilio}")

            # Mostrar un mensaje de confirmación
            QMessageBox.information(self, "Cliente Agregado", "El cliente ha sido agregado exitosamente.")
            
            # Cerrar la ventana después de agregar el cliente
            self.accept()
        else:
            # Mostrar un mensaje de error si los campos están vacíos
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")

