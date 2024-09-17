# Se usan las listas para simular las pilas y colas 
pila=[]
cola=[]

#PILAS LIFO    Último en entrar primero en salir 
# Para implementar una pila, por lo tanto, necesitamos dos operaciones simples:
#   push – agrega un elemento a la parte superior de la pila --> append()
#   pop – elimina el elemento en la parte superior de la pila --> pop()
#push
pila.append(1)
pila.append("Ana")
pila.append("ultimo")
#pop
ultimoelemento=pila.pop() #recibo el valor devuelto en una variabñe
print(ultimoelemento) #
     


#COLAS  FIFO  Primero en entrar primero en salir 
#   Para implementar una cola, por lo tanto, necesitamos dos operaciones simples:
#      enqueue() – agrega un elemento al final de la cola --> append()
#      dequeue()– elimina el elemento al principio de la cola--> pop(0)
#enqueue
cola.append('banana')
cola.append('grapes')
cola.append('mango')
cola.append('orange')
#dequeue
primerelemento=cola.pop(0)
print(primerelemento)

