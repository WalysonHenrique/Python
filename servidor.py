from flask import Flask, jsonify, request

app = Flask(__name__)
dados = []
 
dados.append({
        "Descricao": "Amarelo"
        ,"Quantidade": "20"
        })

@app.route('/')
def hello_world():

    return jsonify(dados)


app.run(host="127.0.0.1",port=5000)