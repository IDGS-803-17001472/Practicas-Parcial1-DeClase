class PiramideAsteriscos:
    #Declaracion de propiedades de clase
    n=0

    #Declaracion de constructor
    def __init__(self,a) :
        self.n = a

    #declaracion de metodos de clase
    def crearPiramide(self):
        for tem in range(int(self.n)):
            asteriscosString = ""
            for asteriscos in range(tem):
                asteriscosString+"*"
                print(asteriscosString)
        for tem2 in range(int(self.n), 0, -1):
            asteriscosString = ""
            for asteriscos in range(tem2):
                asteriscosString = asteriscosString+"*"
                print(asteriscosString)

def main():
    obj=PiramideAsteriscos(input("introduce el tamaño de la piramide"))
    obj.crearPiramide()

if __name__ == "__main__":
    main()