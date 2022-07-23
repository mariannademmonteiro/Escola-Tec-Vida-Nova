# Interação com o usuário: palavra inicial, palpites
## Tratar a palavra de entrada:
## - remover espaço no final
## - converter para maiúsculo
## - evitar caracteres que não sejam letras
# Desenhar tantos _ quantas forem as letras da palavra inicial
# Definir o número máx de palpites errados (chances)
# Solicitar palpites e analisar se certo ou errado:
## Verificaçãso se o palpite é VÁLIDO
# Contar palpites errados: se ultrapassar o max, perde
# Caso o palpite esteja correto:
# - Fazer a letra correta aparecer no lugar do _ correspondente
# Verificar se a letra já foi usada

palavra_inicial = input("Informe a palavra da forca: ")

max_palpites = 6
erros = 0
letras_usadas = []
acertei_tudo = False
letras_corretas = []
max_erros = 6

is_valid = palavra_inicial.isalpha()
if not is_valid:
    print("Essa palavra não contém apenas letras. É INVÁLIDA")
    exit()

palavra_inicial = palavra_inicial.strip().upper()

while erros <= max_erros and not acertei_tudo:
    total_caracteres = len(palavra_inicial)
for i in range(total_caracteres):
    print("_", end=" ")
print()

# Solicitando palpite
palpite = input ("Diga uma letra: ").upper()

palpite_valido = palpite.isalpha() and len(palpite == 1)

while not palpite_valido:
    palpite = input("Seu palpite foi inválido, informe outro: ")
    palpite_valido = palpite.isalpha() and len(palpite == 1)

palpite = palpite.upper()
if palpite in letras_usadas:
    print("Esse palpite já foi. Tente novamente")
else:
    print("Palpite novinho!!")
    letras_usadas.append(palpite)

    if palpite in palavra_inicial:
        print("Boa! Essa letra está na palavra! ")
        letras_corretas.append(palpite)
        
        #Verificar se ganhamos
        for letra in palavra_inicial:
            if letra not in letras_usadas:
                acertei_tudo = False
                break
            else:
                acertei_tudo = True

    else:
        print("Puts, você errou amigão...")
if palpite_valido:
    print("Boa filhão! Mandou bem")
else:
    print("Tá de sacanagem??")
    erros = erros + 1
    print("Erros pemitidos", max_erros - erros)
