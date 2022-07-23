# Pedir uma palavra ao usuário
palavra = input("Digite um palavra qualquer: ")

palavra_invertida = ""

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

print(palavra_invertida)


# Imprimir a palavra invertida
# Exemplo:
# Digite uma palavra qualquer: Banana
# A palavra invertida é: ananaB