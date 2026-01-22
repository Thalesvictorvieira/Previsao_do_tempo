from flask import Flask, render_template, request
from api import CHAVEAPI
import requests
from datetime import datetime
import locale
app = Flask(__name__)
URL_PREVISAO = "https://api.weatherapi.com/v1/forecast.json"
# Português para dias da semana
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

def previsao_do_tempo(cidade: str):
    cidade = cidade.strip().lower()
    parametros = {
        "key": CHAVEAPI,
        "q": cidade,
        "lang": "pt",
        "days": 5
    }
    resposta = requests.get(URL_PREVISAO, params=parametros, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()

    # Tempo atual
    atual = {
        "cidade": dados["location"]["name"],
        "data": datetime.now().strftime("%d de %B de %Y"),
        "temperatura": dados["current"]["temp_c"],
        "umidade": dados["current"]["humidity"],
        "descricao": dados["current"]["condition"]["text"],
        "icone": dados["current"]["condition"]["icon"]
    }

    previsao = []
    for dia in dados["forecast"]["forecastday"]:
        data = datetime.strptime(dia["date"], "%Y-%m-%d")
        previsao.append({
    "dia_semana": data.strftime("%A").capitalize(),
    "temperatura_media": dia["day"]["avgtemp_c"],
    "condicao": dia["day"]["condition"]["text"],
    "icone":dia["day"]["condition"]["icon"]})
    return atual, previsao


@app.route("/", methods=["GET", "POST"])
def index():
    atual = None
    previsao = []

    if request.method == "POST":
        cidade = request.form["cidade"]
        atual, previsao = previsao_do_tempo(cidade)

    return render_template(
        "indexgpt.html",
        atual=atual,
        previsao=previsao
    )


if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=8080,
    debug=True
    )