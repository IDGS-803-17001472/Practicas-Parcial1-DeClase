class OrdenarYClasificar:
    #Declaracion de propiedades de clase
    n=0

    #Declaracion de constructor
    def __init__(self,a) :
        self.n = a

    #declaracion de metodos de clase
    def correr(self):
        lista =[]
        for x in range(int(self.n)):
            lista.append(input("Introduce un dato"))
        lista.sort
        print("Los numeros ordenados son:" )
        print(lista)
        impares = []
        pares = []
        for x in lista:
            if int(x)%2>0:
                impares.append(x)
            else:
                pares.extend(x)
        if len(impares)>0:
            print("los numeros impares son: ")
            print(impares)
        if len(pares)>0:
            print("los numeros pares son: ")
            print(pares)


def main():
    obj=OrdenarYClasificar(input("introduce la cantidad de datos a leer"))
    obj.correr()

if __name__ == "__main__":
    main()