#Fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181...


valor = int(input("Digite o valor limite : "))

a, b = 0, 1

while b < valor:
    print(b)
    a, b = b,a+b