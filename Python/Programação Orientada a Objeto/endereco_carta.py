dados = ["nome", "logradouro", "numero", "complemento", "bairro", "cep", "cidade", "estado"]
dados_usuario = {}

for dado in dados:
    pergunta = "Por favor insisra seu " + dado + ": "
    dados_usuario[dado] = input(pergunta)

carta = """
{nome}
{logradouro}, {numero} {complemento}
{bairro}
{cep} {cidade} {estado}
"""

print(carta.format(
    nome=dados_usuario["nome"],
    logradouro=dados_usuario["logradouro"],
    numero=dados_usuario["numero"],
    complemento=dados_usuario["complemento"],
    bairro=dados_usuario["bairro"],
    cep=dados_usuario["cep"],
    cidade=dados_usuario["cidade"],
    estado=dados_usuario["estado"],
))