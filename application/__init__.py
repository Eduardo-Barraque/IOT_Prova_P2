from weakref import ProxyTypes
from flask import Flask,jsonify
from application.model.entity.detector import Poluicao
import os

app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), 
            template_folder=os.path.abspath("application/view/templates"))

poluicao_list = [Poluicao(44,76,56,42,14,64,22)]

@app.route("/valores", methods=['GET'])
def home():
    dados_list = [item.toJson() for item in poluicao_list ]
    
    return jsonify(dados_list)
