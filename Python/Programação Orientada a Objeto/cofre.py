digitos = [26 ,27 ,41 ,49 ,44 ,7 ,46 ,21 ,31]

a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8

# valores:
numero_0 = digitos[a]
numero_1 = digitos[b]
numero_2 = digitos[c]
numero_3 = digitos[d]
numero_4 = digitos[e]
numero_5 = digitos[f]
numero_6 = digitos[g]
numero_7 = digitos[h]
numero_8 = digitos[i]

for numero_0 in digitos:
    for numero_1 in digitos:
        for numero_2 in digitos:
            soma_numeros = numero_0 + numero_1 + numero_2
            if numero_0 != numero_1 and numero_1 != numero_2 and numero_0 != numero_2:
                if soma_numeros == 100:
                    print(numero_0, numero_1, numero_2)