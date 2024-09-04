
import mysql.connector as mySql


class Database:
    # Genero la apertura y cierre con la Base de Datos 
    def __init__(self):
        self.cnx = mySql.connect(
            host='localhost',
            user='root',
            password='',
            db='banko'
        )
        self.cursor=self.cnx.cursor()
        print("Conexion establecida")

    def commitear(self):
        self.cnx.commit()

    def cerrar(self):
        self.cnx.close()
        print("Conexion Cerrada")


#############################################
# main
#############################################

# db=Database()
# #todos
# db.cursor.execute("select * from cliente")
# clientes=db.cursor.fetchall()
# for cliente in clientes:
#     print(cliente)

# #uno
# id=2
# db.cursor.execute("SELECT * FROM cliente WHERE idCliente='{}'".format(id))
# cliente=db.cursor.fetchone()
# print("cliente id 2",cliente)


# #comiteadoras seriales
# #+1
# query = "INSERT INTO cliente VALUES ('{}','{}','{}')".format(4,"Homero Simpson","Siemp`reviva 123")
# db.cursor.execute(query)
# db.commitear() #que pasa si no comieteo

# #+1 forma2
# query="INSERT INTO cliente VALUES (%s,%s,%s)"
# datos=(5,"Homero Simpson","Siempreviva 123")
# db.curso.execute(query,datos)


# db.cursor.execute("select * from cliente")
# clientes=db.cursor.fetchall()
# print(clientes)

# db.cerrar()



