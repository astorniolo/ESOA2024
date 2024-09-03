
import mysql.connector
from Database import *


#comentario prueba para github
class ClienteDB(Database):
    def __init__(self):
        super().__init__()

    def getALL(self):
        sql= 'SELECT * FROM cliente'
        self.cursor.execute(sql)
        Lista=self.cursor.fetchall()
        return Lista    
    
    def getOne(self,id):
        sql="SELECT * FROM cliente where idCliente='{}'".format(id)
        print(sql)
        self.cursor.execute(sql)
        cliente=self.cursor.fetchone()
        return cliente           

    def nuevo(self, idCliente, clienteNombre, clienteDomicilio):
        sql="INSERT INTO cliente  VALUES  ('{}','{}','{}')".format(idCliente,clienteNombre,clienteDomicilio)
        self.cursor.execute(sql)
        self.connection.commit()

            
    def update(self,idCliente, clienteNombre, clienteDomicilio):
        sql="UPDATE cliente SET clienteNombre = '{}', clienteDomicilio = '{}' WHERE idCliente = '{}'".format(clienteNombre,clienteDomicilio,idCliente)
        self.cursor.execute(sql)
        self.connection.commit()    
        
    
    def delete(self,idCliente): 
        sql="DELETE FROM cliente WHERE idCliente = '{}'".format(idCliente)
        self.cursor.execute(sql)
        self.connection.commit()    
    
    def ya_existe(self,idCliente):
        sql="SELECT * FROM cliente where idCliente='{}'".format(id) 
        cliente=self.cursor.fetchone()
        return cliente != None
    
gestorClientes=ClienteDB()
print(gestorClientes.getALL())
print(gestorClientes.getOne(1))
gestorClientes.nuevo(4,"Homero","Siempre Viva 123")
print(gestorClientes.getALL())
gestorClientes.delete(4)
if gestorClientes.ya_existe(4):
    print("epa no se elimino")
else:
    print("ya jue")