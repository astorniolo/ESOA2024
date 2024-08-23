class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __del__(self):
        print('Método delete llamado')
        #el punto vuelve al origen
        self.x=0
        self.y=0

    def __str__(self) -> str:
        return "Coordenada del punto: ({}:{})".format(self.x,self.y)

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0: print("Primer cuadrante")
        elif self.x<0 and self.y>0: print("Segundo cuadrante")
        elif self.x<0 and self.y<0: print("Tercer cuadrante")
        else: print("Cuarto cuadrante")

    def coordenadasIguales(self,punto):
        return True if (self.x == punto.x  and self.y == punto.y ) else False


