# Pedir uma palavra ao usuário
palavra = input("Digite um palavra qualquer: ")

palavra_invertida = ""
ultimo_index = len(palavra) - 1

for i in range(ultimo_index, -1, -1):
    letra = palavra[i]
    palavra_invertida = palavra_invertida + letra

print(palavra_invertida)


# Imprimir a palavra invertida
# Exemplo:
# Digite uma palavra qualquer: Banana
# A palavra invertida é: ananaB