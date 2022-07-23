# Classe Carta
# Recebe dois atributos: valor e naipe (Copas, Espada, Paus, Ouros)
# Métodos:
# - Revela o naipe e o valor da carta. Como? Imprimindo na teça
# - Validação do naipe e do valor da carta

class Carta:

    NAIPES = ["copas", "ouros", "paus", "espadas"]
    VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
    # VALORES = [str(n) for n in range(2, 11)] + list("AQJK")

    def __init__(self, valor, naipe):
        self.valida_carta(valor, naipe)
        self.valor = valor
        self.naipe = naipe

    def valida_carta(self, valor, naipe):
        if valor not in self.VALORES:
            raise Exception(f"Este valor não é um valor aceito: {valor}")
        if naipe not in self.NAIPES:
            raise Exception(f"Este valor não é um valor aceito: {naipe}")

    def mostrar(self):
        print(f"{self.valor} {self.naipe}")
    
x = Carta("10", "espadas")
x.mostrar()

#{
#    'Paus'    : '\u2663',
#    'Copas'   : '\u2665',
#    'Espadas' : '\u2660',
#    'Ouros'   : '\u2666'
#}