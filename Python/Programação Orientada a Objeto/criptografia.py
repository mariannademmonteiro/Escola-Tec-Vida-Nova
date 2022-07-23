# E -> 3
# A -> 4
# S -> 5


palavra = input("Digite uma palavra: ").upper()

palavra_codificada = ""

for letra in palavra:
    if letra == "A":
        palavra_codificada = palavra_codificada + "4"
    elif letra == "E":
        palavra_codificada = palavra_codificada + "3"
    elif letra == "S":
        palavra_codificada = palavra_codificada + "5"
    elif letra == "J":
        palavra_codificada = palavra_codificada + "K"
    else:
        palavra_codificada = palavra_codificada + letra

print(palavra_codificada)