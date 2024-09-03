import mysql.connector

class Database:
    # Genero la apertura y cierre con la Base de Datos 
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='hepatalgina',
            database='banko'
        )
        self.cursor=self.connection.cursor()
        print("Coneccion establecida")

    def comitear(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()
        print("Cnx Cerrada")

    
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

# bd=Database()
# query="INSERT INTO cliente  VALUES (%s,%s,%s)"
# datos=(4,"Homero Simpson","SiempreViva 123")
# bd.cursor.execute(query,datos)
# bd.comitear()


# query2="Select * from cliente"
# bd.cursor.execute(query2)
# lista=bd.cursor.fetchall()
# print(lista)

# bd.close()