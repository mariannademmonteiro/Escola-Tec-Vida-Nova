precos = {
    "carambola": 6,
    "jaboticaba": 1,
    "melancia": 18,
    
}

mensagem_pergunta_fruta = """
Temos as seguintes frutas:
carambola
jaboticaba
melancia
Qual delas você gostaria?
"""

fruta = input(mensagem_pergunta_fruta).lower()
preco = precos [fruta]
print("O preço unitário dessa fruta é {}".format(preco))


qtd = input("Quantas unidades você gostaria? ")
qtd_int = int(qtd)

total = qtd_int * preco
print("O total deu {} reais".format(total))

valor_pago = int(input("Pagamento em cedula, qual seria?"))

def calcula_troco(total, valor_pago):
    troco = valor_pago - total
    print("Divida: ", total)
    print("Troco: ", troco)
    
calcula_troco(total, valor_pago)