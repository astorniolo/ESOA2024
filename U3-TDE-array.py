##################################################################################
###                            T D E : A  R  R  A  Y                           ###
##################################################################################
# ¿Qué son los arrays y para qué se utilizan?
# El término array(arreglo o vector) se refiere a un tipo de datos o, 
# más concretamente, a un contenedor con:
#        un número predefinido de valores 
#        de un determinado tipo. 
# El tipo de datos permitidos no está limitado; el contenedor también puede contener
# objetos o incluso otros arrays. Sin embargo, la longitud y el tipo de datos 
# deben ser definidos previamente y no pueden ser cambiados posteriormente. 
# El proceso de almacenar los valores dentro del contenedor se llama inicialización.

# Nota
    # Los clásicos arrays descritos anteriormente no existen en Python como tal.
    # Una forma elegante de superar esta limitación es utilizar las llamadas listas 
    # in Python, que tienen una función similar pero las listas de Python pueden 
    # contener diferentes tipos de valores.

# Crear arrays con listas de Python-------------------------------------------------
# UnidadesNavales como variables individuales
unidad_naval1 = "AVES"
unidad_naval2 = "AVIR"
unidad_naval3 = "FRLI"
# UnidadesNavales agrupados en un "array" usando list de python
# definicion por extencion
unidadesNavales = ["AVES", "AVIR", "FRLI"]
unidadesNavales2 = [unidad_naval1 , unidad_naval2 , unidad_naval3 ]
unidadesNavales3 = list()
unidadesNavales3.append("AVES")
unidadesNavales3.append(3.5)
unidadesNavales3.append([1,2,"3"])
unidadesNavales3.append((1,2,3))
print("unidadesNavales3",unidadesNavales3)
# Acceso:
# Acceder a un elemento específico
# Para acceder a un elemento concreto, utiliza el número de índice. 
primero= unidadesNavales[0]
print("primer elemento:",primero)  # AVES
# Acceso y modificacion
unidadesNavales[0] = "AVEStruz"
 
print("primer elemento luego de modificar:",unidadesNavales[0])  
print("unidades navales luego de modificar:",unidadesNavales)

avisos=["AVIR","AVTO","AVBA","AVES","AVIM","AVPA"]
buques=["BHAU","BHCR","BHPD","BHSH"]
corbetas=["CBDR","CBGR","CBGU","CBES","CBRO","CBSP","CBPA","CBRB","CBGO"]
destructores=["DEAB","DELA","DESI","DEHA"]
unidadesNavales[0] = avisos
print("primer elemento luego de modificacion2:",unidadesNavales[0] )  
print("unidades navales luego de modificar2:",unidadesNavales)
unidades_navales_por_tipo=[avisos,buques,corbetas,destructores]
print("unidades navales por tipo",unidades_navales_por_tipo)
#Longitud = cantidad de elementos que contiene en un momento dado 
# len()
# Para establecer la longitud, selecciona el valor más alto de los números de índice previstos y auméntalo en 1. Para obtener la longitud del array en Python, utiliza el método “len ( )”. He aquí un ejemplo:

cantidadUnidadesNavales=len(unidadesNavales)
print("cantidad de elementos de unidadesnavales",cantidadUnidadesNavales)
cantidadUnidadesNavales2= len(unidadesNavales2)
print ("cantidad de elementos de unidadesnavales2",cantidadUnidadesNavales2)

print("la cantidad de avisos  es ",len(unidadesNavales[0]))
#recorrido de un array
print("recorrido for i 11111111111111111111111111111111111111")
for i in range(len(unidades_navales_por_tipo)):
    print(f"i:{i} contiene {unidades_navales_por_tipo[i]}")
print()


#recorrido por tipo de unidad
print("recorrido por tipo 222222222222222222222222222222222222")
for tipo in unidades_navales_por_tipo:
    print(tipo)

#recorrido por unidades de cada tipo
print() 
print("recorrido por tipò y por unidad de cada tipo  33333333333333333333333333333")
for tipo in unidades_navales_por_tipo:
    print(tipo)  
    print("    Unidades individuales")
    for unidad in tipo:
        print("    ",unidad) 

#recorrido por unidades de cada tipo
print() 
print("recorrido por tipò y por unidad de cada tipo  con  for anidados i j  44444444444444444444444444444")
for i in range(len(unidades_navales_por_tipo)):
    print(f"TIPO i:{i} contiene {unidades_navales_por_tipo[i]}")
    print("    Unidades individuales")
    for j in range (len(unidades_navales_por_tipo[i])) :
        print(f"     tipo {i} Unidad {j} => unidades_navales_por_tipo[{i}][{j}] : {unidades_navales_por_tipo[i][j]}") 

              
# Añadir
# para añadir elementos a tu array en Python, 
# lo mejor es utilizar el método “append ( )”.
fragatas=["FRLI"]
submarinos=["SUSA","SUSC","SUSE","SUSF","SUSJ"]

unidades_navales_por_tipo.append(fragatas)
unidades_navales_por_tipo.append(submarinos)

#primer copiarpegar ..... ando ganas crear funcion !!!!!!
#recorrido por unidades de cada tipo
print() 
print("recorrido por tipò y por unidad de cada tipo")
for tipo in unidades_navales_por_tipo:
    print(tipo)  
    print("    Unidades individuales")
    for unidad in tipo:
        print("    ",unidad) 

# recorro un array y lo agrego a otro uno a uno
print("unidadesnavales2",unidadesNavales2)
print ("cantidad de elementos de unidadesnavales2",len(unidadesNavales2))
for submarino in submarinos:
    unidadesNavales2.append(submarino)
print("unidadesnavales2",unidadesNavales2)
print ("cantidad de elementos de unidadesnavales2",len(unidadesNavales2))   
unidadesNavales2*=2
print("unidadesnavales2",unidadesNavales2)
print ("cantidad de elementos de unidadesnavales2",len(unidadesNavales2))  

# Eliminar elementos del array con pop ( ) o remove ( )
# Hay dos formas de eliminar elementos de un array en Python. 
# El primer método es “pop ( )”. 
# en unidadesnavales 2 tenemos en 3º lugar la frli  pero como empiezan en 0 seria el elemnto2
print("unidadesnavales2",unidadesNavales2)
tercero=unidadesNavales2.pop(2)
print("elemento eliminado",tercero)
print("unidadesnavales2",unidadesNavales2)

# El segundo método es “remove ( )”
print("unidadesnavales2",unidadesNavales2)
elto=unidadesNavales2.remove("SUSF")
print("elemento eliminado",tercero)
print("unidadesnavales2",unidadesNavales2)

#ordenar elementos
#recordemos que en unidades navales 2 tenemos los elementod duplicados 
# si quiero eliminar duplicados lo paso a conjunto 
print("unidadesnavales2",unidadesNavales2)
unidadesNavales2=set(unidadesNavales2)
print("unidadesnavales2",unidadesNavales2)
unidadesNavales2=list(unidadesNavales2)
print("unidadesnavales2",unidadesNavales2)

#ordenar
print("unidadesnavales2",unidadesNavales2)
unidadesNavales2.sort()
print("unidadesnavales2",unidadesNavales2)


# Método	        Descripción
# append ( )	    Añade un elemento al final de la lista (ver arriba).
# clear ( )	        Este método elimina todos los elementos de la lista.
# copy ( )	        copy ( ) produce una copia de toda la lista.
# count ( )	        Este método da como resultado el número exacto de elementos con un valor determinado.
# extend ( )	    añade todos los elementos de una lista al final de un array en Python.
# index ( )	        Muestra el número de índice del primer elemento con un valor determinado.
# insert ( )	    Añade un elemento en una posición determinada.
# len ( )	        Con len ( ) se determina la longitud de un array en Python (ver arriba).
# pop ( )	        Con pop ( ) se elimina un elemento en una posición determinada (ver arriba).
# remove ( )	    remove ( ) elimina el primer elemento con un valor determinado.
# reverse ( )	    Utiliza este método para invertir el orden de los elementos de tu array en Python.
# sort ( )	        Con sort ( ) puedes ordenar tu lista.