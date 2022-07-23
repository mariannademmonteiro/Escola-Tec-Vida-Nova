cpf_original = "145.382.206-20"

cpf_sem_validacao = 145382206

cpf_copia = cpf_sem_validacao

total = 0
for peso in range(2, 11):
    digito = cpf_copia % 10
    cpf_copia = cpf_copia // 10
    # digito, cpf_copia = divmod(cpf_copia, 10)
    resultado = digito * peso
    total = total + resultado

total_mod11 = total % 11

digito_ver1 = 11 - total_mod11

print(total_mod11)