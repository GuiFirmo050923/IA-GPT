import requests 

url = "https://viacep.com.br/ws/13456721/json/"

dados = requests.get(url)
endereco = dados.json()

print(endereco)
