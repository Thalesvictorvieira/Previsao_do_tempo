import requests
import os
from dotenv import load_dotenv
from api import CHAVEAPI

load_dotenv()

API_KEY = CHAVEAPI
def get_weather(city):
    #
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": API_KEY,
        "q": city,
        "lang": "pt"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Erro ao acessar a API")

    return response.json()


if __name__ == "__main__":
    city = input("Digite a cidade: ")
    data = get_weather(city)

    print("Cidade:", data["location"]["name"])
    print("Temperatura:", data["current"]["temp_c"], "°C")
    print("Condição:", data["current"]["condition"]["text"])
