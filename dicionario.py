# https://ellibrodepython.com/diccionarios-en-python

# Diccionario
# Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en 
# forma de llave y valor.

# Crear diccionario Python
# Un diccionario en Python es una colección de elementos, 
# donde cada uno tiene una llave key y un valor value. 
# Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value.
# En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.


unidades_navales= {
    "avisos" :["AVIR","AVTO","AVBA","AVES","AVIM","AVPA"],
    "buques":["BHAU","BHCR","BHPD","BHSH"],
    "corbetas":["CBDR","CBGR","CBGU","CBES","CBRO","CBSP","CBPA","CBRB","CBGO"],
    "destructores":["DEAB","DELA","DESI","DEHA"]
}
# imprimir diccionario
print(unidades_navales)


# Otra forma equivalente de crear un diccionario en Python es usando dict() 
# e introduciendo los pares key: value entre paréntesis.
otras_unidades = dict([
       ('fragatas', ["FRLI"]),
       ('submarinos',["SUSA","SUSC","SUSE","SUSF","SUSJ"]),
       ('Documento', 1003882),
       ("dia de la armada","17 de mayo")
 ])
print(otras_unidades)

# Algunas propiedades de los diccionario en Python son las siguientes:
# Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
# Son indexados, los elementos del diccionario son accesibles a través del key.
# Y son anidados, un diccionario puede contener a otro diccionario en su campo value.

#########################################################################
# Acceder y modificar elementos
# Se puede acceder a sus elementos con [] o también con la función get()

print(unidades_navales['avisos'])     
print(unidades_navales.get('avisos')) 

# Para modificar un elemento basta con usar [] con el nombre del key y asignar el valor que queremos.

unidades_navales['avisos'] += ["aves222"]
print(unidades_navales)

# Si el key al que accedemos no existe, se añade automáticamente.
unidades_navales['patrona'] = ["Stella Maris"]
print(unidades_navales)


# Iterar diccionario
# Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras 
# de datos. Para imprimir los key.

# # Imprime los key del diccionario
print(unidades_navales.keys())
for clave in unidades_navales:
    print(clave)

# Se puede imprimir también solo el value.
# Imprime los value del diccionario
for k in unidades_navales:
     print(unidades_navales[k])

# si queremos imprimir el key y el value a la vez.
for clave,valor in unidades_navales.items():
     print(f"clave {clave} , valor {valor} ")


# Los diccionarios en Python pueden anidarse. 
descripcion_uddes={
    {
        "tipo Unidad":"aviso",
        "nombre Unidad": "AVIR",
        "tripulacion": ["Juan Augusto Masmorro","Jose Valiente y Peña"]
    },
    {
        "tipo Unidad":"fragata",
        "nombre Unidad": "FRLI",
        "tripulacion":["Mastropiero Quenunca"]
       
    }
}
print(descripcion_uddes)


# Métodos diccionarios Python      
# clear()
# El método clear() elimina todo el contenido del diccionario.
descripcion_uddes.clear()
print(descripcion_uddes) 

# get(<key>[,<default>])
# El método get() nos permite consultar el value para un key determinado. 
# El segundo parámetro es opcional, y en el caso de proporcionarlo es el valor 
# a devolver si no se encuentra la key.
tripulante={
     "DNI":12345678,
     "nombre tripulante" :"Juan Augusto Masmorro",
     "edad":35
}

print(tripulante.get('DNI')) 
print(tripulante.get('direccion', 'No encontrado')) 

# items()
# El método items() devuelve una lista con los keys y values del diccionario.
# Si se convierte en list se puede indexar como si de una lista normal se tratase,
# siendo los primeros elementos las key y los segundos los value.

itemsTripulante=tripulante.items()
print(itemsTripulante)
print(list(itemsTripulante))
print(list(itemsTripulante)[0][0]) 

# keys()
# El método keys() devuelve una lista con todas las keys del diccionario.
clavesTripulante=tripulante.keys()
print(clavesTripulante)

# values()
# El método values() devuelve una lista con todos los values o valores del diccionario.
valoresTripulante=tripulante.keys()
print(valoresTripulante)

print(list(tripulante.values())) 

# pop(<key>[,<default>])
# El método pop() busca y elimina la key que se pasa como parámetro
# y devuelve su valor asociado.
# Daría un error si se intenta eliminar una key que no existe.

clave1 = tripulante.pop("DNI")
print(tripulante)
print(clave1)
# También se puede pasar un segundo parámetro que es el valor a devolver 
# si la key no se ha encontrado. En este caso si no se encuentra no habría error.


# popitem()
# El método popitem() elimina de manera aleatoria un elemento del diccionario.
tripulante.popitem()
print(tripulante)

# update(<obj>)
# El método update() se llama sobre un diccionario y tiene como entrada otro diccionario.
# Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.

# d1.update(d2)
# print(d1)
# #{'a': 0, 'b': 2, 'd': 400}

trip1={ "DNI":12345678,"nombre tripulante" :"Juan Augusto Masmorro"},
trip2={"DNI":1333333,"nombre tripulante" :"Jose Valiente y Peña", "edad":37}               
trip1.update(trip2)
print(trip1)
