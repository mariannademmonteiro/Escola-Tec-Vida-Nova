def leitor_de_csv(filename):
    with open (filename, "r") as f:
        header = f.readline().strip().split(",")

        dados = []
        for linha in f:
            linha = linha.strip()
            linha_lista = linha.split(",")
            linha_dict = ()
            for i in range(len(linha_lista)):
                chave = header[i]
                valor = linha_lista[i]
                linha_dict[chave] = valor
            dados.append(linha_dict)

        return dados


filename = "data/pessoas.csv"
dados_processados = leitor_de_csv(filename)
print(dados_processados)