
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

    def close(self):
        self.connection.close()
        print("Cnx Cerrada")


# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# INSERT INTO `banko`.`cliente`  VALUES (1,"Margerit Simpson","SiempreViva 123");
# INSERT INTO `banko`.`cliente`  VALUES (2,"Lisa Simpson","SiempreViva 123");
# INSERT INTO `banko`.`cliente`  VALUES (3,"Bart Simpson","SiempreViva 123");

bd=Database()
bd.close()


