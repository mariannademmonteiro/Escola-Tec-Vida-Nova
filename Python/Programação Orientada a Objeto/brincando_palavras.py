# Faça o download e salve seu conteúdo num arquivo chamado “palavras.txt” - https://www.ime.usp.br/~pf/dicios/
# Faça uma função para cada item abaixo:
# Conte quantas palavras há no arquivo
# Conte quantas vezes cada letra do alfabeto aparece no arquivo
# Conte quantas palavras começam com cada letra do alfabeto
# Identifique as palavras começam com as mesmas 3 letras do seu nome e salve-as num arquivo separado
# Identifique as palavras que possuem todas as letras do seu nome e salve-as num arquivo separado
# Identifique todas as palavras que são palíndromos e salve-as num arquivo separado

lista_palavras = []
with open(r"brincando_palavras.txt", "r", encoding="utf-8") as arquivo_portugues:
    for linha in arquivo_portugues:
        lista_palavras.append(linha.upper())

def conta_palavras(lista_palavras):
    return len(lista_palavras)

contagem_palavras = conta_palavras(lista_palavras)
print(f"O total de palavras é\n: {contagem_palavras}")

def conta_letras(lista_palavras):
    dicionario_acumula = {}
    
    for palavra in lista_palavras:       
        lista_letras = list(palavra)        
        for letra in lista_letras:           
            if letra not in dicionario_acumula:
                dicionario_acumula[letra] = 1               
            else:
                dicionario_acumula[letra] += 1                
    return dicionario_acumula

contagem_letras = conta_letras(lista_palavras)
print("O acumulado de aparicoes por letra é:\n")
print(contagem_letras)

def conta_inicio_palavra(lista_palavras):
    dicionario_acumula = {}
    for palavra in lista_palavras:
        if palavra[0] not in dicionario_acumula:
            dicionario_acumula[palavra[0]] = 1
        else:
            dicionario_acumula[palavra[0]] += 1
    return dicionario_acumula

contagem_inicia_palavra = conta_inicio_palavra(lista_palavras)
print("O acumulado de palavras iniciadas por cada letra é:\n")
print(contagem_inicia_palavra)

def conta_palavra_tres_letras(lista_palavras, inicias_nome):
    with open("palavras_iniciais.txt", "a", encoding="utf-8") as arquivo_escrita:
        for palavra in lista_palavras:
            if palavra[:3] == inicias_nome:
                arquivo_escrita.write(palavra)

conta_palavra_tres_letras(lista_palavras, inicias_nome="MAR")

def conta_palavra_igual_nome(lista_palavras, nome):
    with open("palavras_igual_nome.txt", "a", encoding="utf-8") as arquivo_escrita:
        for palavra in lista_palavras:
            if palavra[:3] == nome:
                arquivo_escrita.write(palavra)

conta_palavra_igual_nome(lista_palavras, nome="MARIANNA")


