# 🌦️ Weather Web App – Flask

Aplicação web desenvolvida em **Python + Flask** que exibe informações climáticas em tempo real utilizando a API do www.weatherapi.com.

Este projeto foi criado com foco em aprendizado prático de:
- Consumo de APIs externas
- Desenvolvimento web com Flask
- Estruturação de projetos Python
- Boas práticas para portfólio no GitHub

---

## 🚀 Funcionalidades

- 🔍 Busca de clima por cidade
- 🌡️ Exibição de temperatura atual
- 💧 Umidade do ar
- 🌬️ Velocidade do vento
- ☁️ Condição climática
- 🎨 Interface web simples e responsiva

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**
- **API weatherapi**

---

## 📁 Estrutura do Projeto

```text
weather-app/
│
├── app.py
├── api.py              # Arquivo com a chave da API (NÃO versionar)
├── requirements.txt
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
---
```

🔑 Configuração da API (IMPORTANTE)

Este projeto não inclui a chave da API por motivos de segurança.

Passo a passo:

Acesse o site oficial:
👉 www.weatherapi.com

Crie uma conta gratuita

Gere sua API Key

No diretório raiz do projeto, crie um arquivo chamado: api.py
Dentro do arquivo api.py, adicione:

API_KEY = "SUA_CHAVE_AQUI"
▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/weather-app.git
cd weather-app

2️⃣ Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute o servidor
python app.py


Acesse no navegador:

http://127.0.0.1:5000


Ou, para acesso em outros dispositivos da rede:

http://IP_DA_SUA_MAQUINA:5000

🌐 Acesso pela Rede Local

O servidor Flask está configurado para rodar com:

app.run(host="0.0.0.0", port=5000, debug=True)


Isso permite acesso por outros dispositivos na mesma rede, desde que:

Firewall permita a porta 5000

Os dispositivos estejam na mesma rede local
