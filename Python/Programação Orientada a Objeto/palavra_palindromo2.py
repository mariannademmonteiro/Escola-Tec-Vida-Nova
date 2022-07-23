def inverte_palavra(p):
    return p[::-1]

# Pedir uma plavra ou frase ao usuário
palavra = input("Digite uma frase ou palavra: ")

eh_palindromo = True
for i in range(len(palavra)):
    j = len(palavra) -1 - i
    letra_i = palavra[i]
    letra_j = palavra[j]

    if letra_i != letra_j:
        eh_palindromo = False
        break

if eh_palindromo:
    print("Parabéns, você digitou um palíndromo")
else:
    print("Puts... não é um palíndromo")