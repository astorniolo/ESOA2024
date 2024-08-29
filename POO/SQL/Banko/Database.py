


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

