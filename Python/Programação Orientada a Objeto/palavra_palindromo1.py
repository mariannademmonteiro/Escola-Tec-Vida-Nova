def inverte_palavra(p):
    return p[::-1]

# Pedir uma plavra ou frase ao usuário
palavra = input("Digite uma frase ou palavra: ")

palavra_invertida = inverte_palavra(palavra)
# Dizer pro usuário se a palavra/frase é palíndromo

eh_palindromo = palavra == palavra_invertida # Faça alguma mágica para calcular

if eh_palindromo:
    print("Parabéns, você digitou um palíndromo")
else:
    print("Puts... não é um palíndromo")