print("BEM VINDO AO CINEMARI")
num_poltrona = int((input("Digite a quantidade poltronas no CINEMARI: "))) 

sala = [] 

for x in range(num_poltrona): 
    sala.append(x+1)
print(sala)

poltrona= int(input("\n\nEscolha uma poltrona disponível: ")) 

while (sala[x] == num_poltrona):

    for x in range(num_poltrona): 
        if (poltrona == sala[x]):
            sala[x] = 'X'
            if sala[x] == 'X':
                print(sala)

    print("Poltrona",poltrona, "ocupada, por favor escolher outra!!!") 

    print("\n", sala)
    poltrona= int(input("Escolher uma poltrona disponivel: ")) 

print("\nTODAS AS POLTRONAS FORAM OCUPADAS, BOM FILME") 