from api import CHAVEAPI
import requests

ChaveApi = CHAVEAPI
def ConsultaCLima(Cidade="são paulo"):
    """
    Como funciona: Primeiro define a URL que sera solocitado a informacao o clima.
    Depois define os parametros que serao enviados na requisicao.
    Por ultimo a requisicao retorna os dados em um json.
    """
    Url = "https://api.weatherapi.com/v1/current.json"
    
    parametros = {
        "Key":ChaveApi,
        "q":Cidade,
        "lang":"pt"
    }
    RESPOSTA = requests.get(Url,params=parametros)
    #Converte a resposta da requisição de um Json em um dicionario Python
    data = RESPOSTA.json()

    if RESPOSTA.status_code != 200:
        raise Exception("Erro ao acessar a API")

    
    
    print("Cidade:",data["location"]["name"])
    print("Temperatura:",data["current"]["temp_c"],"°C")
    print("Condição:",data["current"]["condition"]["text"])
    print("Umidade relativa do ar",data["current"]["humidity"],"%")

#Cidade = input("Digite a cidade: ")
Cidade = "CONTAGEM"
ConsultaCLima(Cidade)

#Jogar as respostas dentro de uma vaiavel para depois fazer o usuario escolher dentro de uma interface grafica