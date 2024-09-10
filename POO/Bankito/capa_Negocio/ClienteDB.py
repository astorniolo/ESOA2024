from capa_Negocio.Database import *

class ClientDB(Database):
    def __init__(self):
        bd="banko"
        super().__init__()
    
    def traer_Todos(self):
        query="Select * from cliente"
        self.cursor.execute(query)
        lista=self.cursor.fetchall()
        return lista
    
    def traer_uno(self,id):
        query=f"SELECT * FROM cliente where idCliente={id}"
        self.cursor.execute(query)
        cliente=self.cursor.fetchone()
        return cliente if cliente else None
    
    def crear_nuevo(self,id,nombre,direccion):
        query="INSERT INTO cliente  VALUES (%s,%s,%s)"
        datos=(id,nombre,direccion)
        self.cursor.execute(query,datos)
        self.comitear()
    
    def actualizar(self,id,nombre,direccion):
        query="UPDATE cliente SET clienteNombre = %s, clienteDomicilio = %s WHERE idCliente = %s"
        datos=(nombre, direccion, id)
        self.cursor.execute(query,datos)
        self.comitear()

    def borrar(self,id):
        query=f"DELETE FROM cliente WHERE idCliente={id}"
        self.cursor.execute(query)
        self.comitear()
    
    def proximoId(self):
        query=f"SELECT count(IdCliente) FROM banko.cliente"
        self.cursor.execute(query)
        ultimo=self.cursor.fetchone()
        return ultimo[0] + 1  if ultimo else 1
#-------------------
# gestioncliente=ClientDB()
# print(gestioncliente.proximoId())
# listacliente=gestioncliente.traer_Todos()
# print(listacliente)
# cliente4=gestioncliente.traer_uno(4)
# print(cliente4)
# gestioncliente.crear_nuevo(5,"Magie Simpson","Siempre Viva 123")
# gestioncliente.actualizar(5,'Magie Simpson','SiempreViva 1234')
# gestioncliente.borrar(5)
# print(gestioncliente.traer_Todos())
#gestioncliente.close()