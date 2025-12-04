import requests

cep = input ("Digite o seu CEP (apenas números): ")

while len (cep) != 8 or not cep.isdigit():
    print ("CEP incorreto, digite novamente apenas os números.")
    cep = input ("Digite o seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

dados = resposta.json()

cep_tratado = {
    "cep": dados.get("cep"),
    "logradouro": dados.get("logradouro"),
    "complemento": dados.get("complemento"),
    "bairro": dados.get("bairro"),
    "localidade": dados.get("localidade"),
    "uf": dados.get("uf")
}

print(cep_tratado)