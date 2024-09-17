from PySide6.QtWidgets import QApplication, QMainWindow,QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget
import sys
from capa_vista.VentanaListado2_ui import Ui_VentanaListadoDeClientes
from capa_Negocio.ClienteDB import *
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QStringListModel, QTimer, QTime

class VentanaListado2(QDialog,Ui_VentanaListadoDeClientes):
    def __init__(self):
        super(VentanaListado2, self).__init__()

        # Llamar al método setupUi para inicializar los widgets definidos en el archivo .ui
        self.setupUi(self)

        # Establecer título y dimensiones de la ventana      
        self.setWindowTitle("Poblando diferentes widgets")
        self.setGeometry(100, 100, 900, 700)

        #traer los cliente desde el backend
        gestionClientes=ClientDB()
        self.clientes = gestionClientes.traer_Todos()

        # Botón para POBLAR
        self.pushButton_4.setText("Poblar...populate....llenar")
        self.pushButton_4.clicked.connect(self.poblar)

        # Botón para llenar Combo
        self.pushButton_5.setText("Poblar Combo Box con los nombres")
        self.pushButton_5.clicked.connect(self.poblar_combobox)
        

        # Inicializo Valores del DIAL
        self.dial.setMinimum(0)
        self.dial.setMaximum(20)
        self.dial.setValue(10)  # Valor inicial
        self.dial.valueChanged.connect(self.actualizar_valor_dial)

        #timer 
        # Inicializo valores del widget QLCDNumber
        self.lcdNumber.setDigitCount(8)  # Para mostrar formato HH:mm:ss
        self.lcdNumber.setStyleSheet("background-color: black; color: green;")  # Estilo LCD
        # Crear un temporizador que actualice cada segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mostrar_hora)
        self.timer.start(1000)  # Actualización cada 1 segundo (1000 ms)
        # Mostrar la hora al iniciar la ventana
        self.mostrar_hora()

        # otros eventos
        self.tableView.clicked.connect(self.on_cell_clicked)
        self.tableView.doubleClicked.connect(self.on_cell_double_clicked)
        

    def on_cell_clicked(self, index):
        fila = index.row()
        columna = index.column()
        valor = index.data()  # Obtiene el valor de la celda
        print(f"Clic en fila {fila}, columna {columna}, valor: {valor}")

    def on_cell_double_clicked(self, index):
        fila = index.row()
        columna = index.column()
        valor = index.data()  # Obtiene el valor de la celda
        print(f"Doble clic en fila {fila}, columna {columna}, valor: {valor}")

    def poblar(self):
        self.poblar_tableview()
        self.poblar_listview()
        self.poblar_columnview()

    def poblar_tableview(self):
        # Crear el modelo para el TableView
        modelo = QStandardItemModel()
        modelo.setHorizontalHeaderLabels(["Id", "Nombre", "Domicilio"])

        # Agregar los datos de la lista de clientes al modelo
        for cliente in self.clientes:
            fila = [
                QStandardItem(str(cliente[0])),  # Id
                QStandardItem(cliente[1]),  # Nombre
                QStandardItem(cliente[2])  # Domicilio
            ]
            modelo.appendRow(fila)

        # Asignar el modelo al TableView
        self.tableView.setModel(modelo)

    def poblar_combobox(self):
        # Agregar los nombres de los clientes al ComboBox
        for cliente in self.clientes:
            self.comboBox.addItem(cliente[1])
    
    def poblar_listview(self):
        # Crear un modelo de cadena para el ListView
        modelo = QStringListModel()
        nombres = [cliente[1] for cliente in self.clientes]  # Solo los nombres
        modelo.setStringList(nombres)

        # Asignar el modelo al ListView
        self.listView.setModel(modelo)

    def poblar_columnview(self):
        # Crear el modelo para el ColumnView
        modelo = QStandardItemModel()

        # Agregar datos jerárquicos al modelo
        for cliente in self.clientes:
            cliente_item = QStandardItem(cliente[1])  # Nombre del cliente
            domicilio_item = QStandardItem(cliente[2])  # Domicilio del cliente
            cliente_item.appendRow(domicilio_item)  # Relación jerárquica
            modelo.appendRow(cliente_item)

        # Asignar el modelo al ColumnView
        self.columnView.setModel(modelo)

    def actualizar_valor_dial(self):
        # Actualizar la etiqueta con el valor actual del dial
        valor = self.dial.value()
        self.valorDIAL.setText(f"Valor del dial: {valor}")

    def mostrar_hora(self):
        # Obtener la hora actual del sistema
        hora_actual = QTime.currentTime()
        # Formatear la hora en HH:mm:ss
        hora_formateada = hora_actual.toString("HH:mm:ss")
        # Establecer la hora en el widget QLCDNumber
        self.lcdNumber.display(hora_formateada)
