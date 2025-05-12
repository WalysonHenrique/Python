import requests
from pprint import pprint
def consultar():
    # Substitua <URL pública do túnel> pelo valor fornecido pelo Ngrok
    url_base = "http://127.0.0.1:5000"

    # Constrói a URL completa para o endpoint da API
    endpoint = '/'
    url = url_base + endpoint

    response = requests.get(url)
    dados = []
    if response.status_code == 200:
        dados = response.json()
        print(dados[0]["Descricao"])
        #data = response.json()
        #print(data)
    else:
        print('Erro ao consumir a API:', response.status_code)
        
def viacepe():
    dados = []
    url = 'https://viacep.com.br/ws/29105163/json'
    response = requests.get(url)

    if response.status_code == 200:
        dados.append({
            'Logradouro':response.json()['logradouro'],
            'Bairro':response.json()['bairro'],
            'Cidade':response.json()['localidade'],
            'UF':response.json()['uf']
        })
        for dado in dados:
            pprint(dado)        
    else:
        print('Erro ao acessar')
    
viacepe()