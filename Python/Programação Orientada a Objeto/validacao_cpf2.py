cpf_usuario = input("Digite seu CPF (Apenas números, sem . ou -): ")

print(cpf_usuario)
cpf_usuario_tratado = ""
for char in cpf_usuario:
    if char.isnumeric():
        cpf_usuario_tratado = cpf_usuario_tratado + char
print(cpf_usuario_tratado)

cpf_original = cpf_usuario[:9] #sting 14538220620

cpf_sem_validacao = int(cpf_original) # 145382206
print("Documento sem validação: ", cpf_sem_validacao)

cpf_copia = cpf_sem_validacao

# Cálculo do primeiro digito verificador
total = 0
for peso in range(2, 11):
    digito = cpf_copia % 10
    cpf_copia = cpf_copia // 10
    # digito, cpf_copia = divmod(cpf_copia, 10)
    resultado = digito * peso
    total = total + resultado

total_mod11 = total % 11

digito_ver1 = 11 - total_mod11

# Cálculo do primeiro digito verificador
cpf_validacao_dig1 = cpf_sem_validacao*10 + digito_ver1
print("Documento com 1 digito verificador", cpf_validacao_dig1)

cpf_copia = cpf_validacao_dig1

# Cálculo do segundo digito verificador
total = 0
for peso in range(2, 11):
    digito = cpf_copia % 10
    cpf_copia = cpf_copia // 10
    # digito, cpf_copia = divmod(cpf_copia, 10)
    resultado = digito * peso
    total = total + resultado

total_mod11 = total % 11

digito_ver1 = 11 - total_mod11

digito_ver2 = 0

# Cálculo do segundo digito verificador
cpf_validado = cpf_sem_validacao*10 + digito_ver2
print("Documento com 2 digitos verificadores", cpf_validado)

cpf_validado_str = str(cpf_validado)
if len(cpf_validado_str) < 11:
    zeros_qtd = 11 - len(cpf_validado_str)
    for i in range(zeros_qtd):
        cpf_validado_str = "0" + cpf_validado_str

if cpf_validado_str == cpf_usuario_tratado:
    print("Este CPF é válido!")
else:
    print("ESSE CPF NÃO É VALIDO!!!!!")



