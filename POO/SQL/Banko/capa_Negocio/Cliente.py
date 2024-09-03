import pymysql
from Database import *

class ClienteDB(Database):
    def  __init__(self):
        super().__init__()
    
    def getAll(self):
        query = "SELECT * FROM cliente"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getOne(self,id):
        query=f"SELECT * FROM cliente WHERE idCliente={id}"
        self.cursor.execute(query)
        cliente=self.cursor.fetchone()
        return cliente
    
    def nuevo(self, id , nombre, domicilio):
        query = "INSERT INTO cliente VALUES (%s,%s,%s)"
        self.cursor.execute(query, (id, nombre, domicilio))
        self.commitear()

    def actualizar(self, id, nombre, domicilio):
        query = "UPDATE cliente SET clienteNombre = %s, clienteDomicilio = %s WHERE idCliente = %s"
        self.cursor.execute(query, (nombre, domicilio, id))
        self.commitear()

    def eliminar(self, id):
        query = f"DELETE FROM cliente WHERE idcliente = {id}"
        self.cursor.execute(query)
        self.commitear()

# gestionclientes=ClienteDB()
# listaclientes=gestionclientes.getAll()
# print(listaclientes)

# unCliente=gestionclientes.getOne(1)
# print("un Cliente----------------------")
# print(unCliente)
# for cliente in listaclientes:
#     print(cliente)

# gestionclientes.nuevo(4,"Homero Simpson","SiempreViva 123")
# print(gestionclientes.getAll())

# gestionclientes.actualizar(5,"Maggie Simpson","SiempreViva 123456789") 
# print(gestionclientes.getAll())

# gestionclientes.eliminar(5)
# print(gestionclientes.getAll())