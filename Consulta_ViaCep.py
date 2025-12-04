import requests
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()



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

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexao.cursor()

sql = """
INSERT INTO dados_cep (cep, logradouro, bairro, localidade, uf)
VALUES (%s, %s, %s, %s, %s)
"""

valores = (
    cep_tratado["cep"],
    cep_tratado["logradouro"],
    cep_tratado["bairro"],
    cep_tratado["localidade"],
    cep_tratado["uf"]
)

cursor.execute(sql, valores)
conexao.commit()

print("O Cep foi inserido no banco de dados com sucesso!")