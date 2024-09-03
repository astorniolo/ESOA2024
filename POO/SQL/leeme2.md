Introducción a la Arquitectura en Tres Capas

La arquitectura en tres capas es un patrón de diseño de software que divide la aplicación en tres partes principales:
    Capa de Presentación (Interfaz de Usuario - UI)
    Capa de Lógica de Negocio (Business Logic)
    Capa de Acceso a Datos (Data Access Layer - DAL)
Cada capa tiene responsabilidades distintas y se comunica con las demás para lograr un funcionamiento cohesivo. Esta arquitectura mejora la modularidad, facilita el mantenimiento y permite una mejor reutilización del código.

1. Capa de Acceso a Datos (DAL)
Responsabilidad:
La DAL es responsable de interactuar directamente con la base de datos. Aquí es donde se realizan operaciones CRUD (Create, Read, Update, Delete) con la base de datos MySQL.

Pasos a seguir:
    Instalar MySQL Connector: Necesitas instalar el conector de MySQL para Python.
        pip install mysql-connector-python
    Implementar la DAL: Esta capa contendrá funciones para cada operación CRUD. Aquí hay un ejemplo básico para una tabla llamada Usuarios:

Copiar código
import mysql.connector

class UsuarioDAL:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def crear_usuario(self, nombre, edad):
        query = "INSERT INTO Usuarios (Nombre, Edad) VALUES (%s, %s)"
        self.cursor.execute(query, (nombre, edad))
        self.conn.commit()

    def leer_usuarios(self):
        query = "SELECT * FROM Usuarios"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def actualizar_usuario(self, id, nombre, edad):
        query = "UPDATE Usuarios SET Nombre = %s, Edad = %s WHERE ID = %s"
        self.cursor.execute(query, (nombre, edad, id))
        self.conn.commit()

    def eliminar_usuario(self, id):
        query = "DELETE FROM Usuarios WHERE ID = %s"
        self.cursor.execute(query, (id,))
        self.conn.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()

2. Capa de Lógica de Negocio (Business Logic)
Responsabilidad:
Esta capa maneja la lógica de la aplicación, actuando como un intermediario entre la DAL y la UI. Aquí es donde decides cómo se manipulan los datos antes de presentarlos o después de recibirlos de la UI.

Implementación:

class UsuarioBL:
    def __init__(self, usuario_dal):
        self.usuario_dal = usuario_dal

    def agregar_usuario(self, nombre, edad):
        # Validaciones o lógica adicional
        self.usuario_dal.crear_usuario(nombre, edad)

    def obtener_usuarios(self):
        return self.usuario_dal.leer_usuarios()

    def modificar_usuario(self, id, nombre, edad):
        # Validaciones o lógica adicional
        self.usuario_dal.actualizar_usuario(id, nombre, edad)

    def eliminar_usuario(self, id):
        self.usuario_dal.eliminar_usuario(id)

3. Capa de Presentación (UI) usando PyQt
Responsabilidad:
La capa de presentación es la interfaz gráfica que interactúa con el usuario. PyQt es una biblioteca de Python que permite crear interfaces gráficas de usuario (GUIs).

Instalación de PyQt:
    pip install PyQt5
Implementación:
Aquí tienes un ejemplo básico de cómo podrías implementar una interfaz para mostrar usuarios en una tabla:


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

class UsuarioUI(QWidget):
    def __init__(self, usuario_bl):
        super().__init__()
        self.usuario_bl = usuario_bl
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Gestión de Usuarios')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        btn_cargar = QPushButton('Cargar Usuarios')
        btn_cargar.clicked.connect(self.cargar_usuarios)
        layout.addWidget(btn_cargar)

        self.setLayout(layout)

    def cargar_usuarios(self):
        usuarios = self.usuario_bl.obtener_usuarios()
        self.table.setRowCount(len(usuarios))
        self.table.setColumnCount(3)  # Asumiendo 3 columnas: ID, Nombre, Edad

        for i, usuario in enumerate(usuarios):
            for j, dato in enumerate(usuario):
                self.table.setItem(i, j, QTableWidgetItem(str(dato)))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Configura la DAL, BL y UI
    usuario_dal = UsuarioDAL(host='localhost', user='root', password='password', database='mi_bd')
    usuario_bl = UsuarioBL(usuario_dal)
    ui = UsuarioUI(usuario_bl)

    ui.show()
    sys.exit(app.exec_())

Resumen
DAL: Interactúa con la base de datos (MySQL).
BL: Aplica la lógica del negocio, validaciones y orquestación de operaciones CRUD.
UI: Interface gráfica creada con PyQt que permite al usuario interactuar con la aplicación.
Requisitos de Instalación:
MySQL: Base de datos.
MySQL Connector: Conexión entre Python y MySQL.
bash
Copiar código
pip install mysql-connector-python
PyQt5: Biblioteca para crear la interfaz gráfica.
bash
Copiar código
pip install PyQt5
Este enfoque modular hace que tu aplicación sea más fácil de mantener y escalar. ¿Te gustaría profundizar en algún aspecto en particular?