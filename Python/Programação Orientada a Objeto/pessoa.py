class pessoa:

    def __init__(self, nome, sobrenome):
        x = nome
        y = sobrenome
        # Salvar o nome e o sobrenome em "algum lugar"

    def dizer_ola(self):
        # Usar o nome e sobre nome para fazer uma saudação
        print("Olá, eu sou o {} {}".format(x, y))

fulano = pessoa(nome, sobrenome)
fulano.dizer_ola()