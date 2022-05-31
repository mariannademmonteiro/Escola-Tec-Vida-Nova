#IR

nome = str(input("Digite seu nome : "))

rendabruta = float(input("Digite sua renda bruta : "))

if rendabruta <= 1903.98:
    imposto = 0
    print("Você não terá que declarar imposto de renda")

elif rendabruta >= 1903.99 and rendabruta <= 2826.65:
    imposto = 7.5

elif rendabruta >= 2826.66 and rendabruta <= 3371.05:
    imposto = 15.0

elif rendabruta >= 3371.06 and rendabruta <= 4664.68:
    imposto = 22.5

elif rendabruta >= 4664.69:
    imposto = 27.5 

rendaliquida = rendabruta - (rendabruta * (imposto / 100))

print("Sr'a' {} \nRenda bruta: {} \nRenda liquida {:.2f}".format(nome, rendabruta, rendaliquida))