picas = "\u2660"
corazon = "\u2665"
diamantes = "\u2666"
trebol = "\u2663"


class baraja:

    def __init__(self,tantos,palo):
        self.total = total
        self.palos = palo
    
    def __str__(self):
        return "[{}-{}]".format(self.tantos,self.palos)

class Carta:
    palos = ["\u2660","\u2665","\u2666", "\u2663"]
    tantos = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    self.mazo = []
    for j in tantos:
        for h in palos:
        cartas = Carta(j,h)
        self.mazo.append(cartas)

    def mostrar_baraja(self):
        for num,Carta in enumerate(self.mazo):
            if num % 4 != 0:
                print(carta, end=" ")
            else:
                print(Carta)
        print()

baraja = baraja()
baraja.mostrar_baraja()






    