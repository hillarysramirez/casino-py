picas = "\u2660"
corazon = "\u2665"
diamantes = "\u2666"
trebol = "\u2663"


class Cartas:

    def __init__(self,tanto,palo):
        self.tanto = tanto
        self.palo = palo
    
    def __str__(self):
        return "[{}-{}]".format(self.tanto,self.palo)

class Baraja:
    def __init__(self):
        palos = ["\u2660","\u2665","\u2666", "\u2663"]
        tantos = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.mazo = []
        for j in tantos:
            for h in palos:
                carta = Cartas(j,h)
                self.mazo.append(carta)

    def mostrar_baraja(self):
        print()
        for num,carta in enumerate(self.mazo):
            if (num-3) % 4 != 0:
                print(carta, end=" ")
            else:
                print(carta)
        print()

Baraja = Baraja()
Baraja.mostrar_baraja()





    