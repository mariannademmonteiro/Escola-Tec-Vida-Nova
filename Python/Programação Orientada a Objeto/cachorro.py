class cachorro:

    def __init__(self, nome, peso, cidade):
        self.nome = nome
        self.peso = peso
        self.cidade = cidade
        self.categoria_peso = self.categoria_peso()

    def classifica_peso(self):
        peso = self.peso
            if peso < 6