print("BEM VINDO AO BOLICHE MARI")

def minha_pista(pinos):
    for pinos_bol in pinos:
        print(pinos_bol, end= '')
    print()
        
pista = [
    'I', ' ', 'I', ' ', 'I', ' ', 'I', '\n', 
    ' ', 'I', ' ', 'I', ' ', 'I', ' ', '\n',
    ' ', ' ', 'I', ' ', 'I', ' ', ' ','\n',
    ' ', ' ', ' ', 'I', ' ', ' ', ' '
]

posicao_pinos = {
    "1": 27,
    "2": 20,
    "3": 18,
    "4": 13,
    "5": 11,
    "6": 9,
    "7": 6,
    "8": 4,
    "9": 2,
    "10": 0,
}

minha_pista(pista)

jogadas = []

while True:
    valor = input("DIGITE O PINO QUE DESEJA DERRUBAR PARA COMEÇARMOS A JOGAR:\n")
    if not valor:
        break
    if valor in jogadas:
        print("PINO JÁ DERRUBADO, TENTE NOVAMENTE!!!")
        continue
    else:
        jogadas.append(valor)

    indice = posicao_pinos [valor]

    pista[indice] = " "

    if "I" in pista:
        minha_pista(pista)
    else:
        print("STRIKE...PARABÉMS VOCÊ DERRUBOU TODOS OS PINOS!!!")
        break