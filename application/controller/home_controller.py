from flask import jsonify, request
from application.model.entity.detector import Poluicao
from datetime import datetime
import json
from application import app

@app.route("/valores", methods=['GET'])
def home():
    with open('dados.json', 'r') as var:
        dados_json = json.load(var) 
    return jsonify(dados_json)

@app.route("/valores", methods=['POST'])
def add_Medida():
    id = request.json.get("Detector", None)
    data = datetime.strptime(request.json.get("data", None), "%d/%m/%Y %H:%M")
    ozonio = int(request.json.get("Ozonio", None))
    material_particulado = int(request.json.get("Material Particulado", None))
    monox_carbono = int(request.json.get("Monoxido de Carbono", None))
    ox_Nitroso = int(request.json.get("Oxido Nitroso", None))
    gas = int(request.json.get("Gas", None))
    temperatura = int(request.json.get("Temperatura", None))
    umidade = int(request.json.get("Umidade", None))
    new_detector = Poluicao(id, data, ozonio,material_particulado , monox_carbono, ox_Nitroso, gas, temperatura, umidade)
    with open('dados.json', 'r') as var:
        new_json =[new_detector.toJson()]
        dados_json = json.load(var)+ new_json
        
    with open('dados.json', 'w') as var:
        json.dump(dados_json, var)
        
    return new_detector.toJson(), 201


@app.route("/valores/id/<id>", methods=['GET'])
def view_valor(id):
    view_list = []
    with open('dados.json', 'r') as var:
        dados_json = json.load(var)
        
    for medida in dados_json:
        if medida.get("Detector") == id:
            view_list.append(medida)

    if view_list == []:
        return jsonify({"error": "Id não encontrado"}), 404
    
    else:
        return jsonify(view_list)


@app.route("/valores/data/<datas>", methods=['GET'])
def view_data(datas):
    data_list = []
    datas = datetime.strptime(datas,"%d-%m-%Y").date()
    with open('dados.json', 'r') as var:
        datas_json = json.load(var)
        
    for medida in datas_json:
        medida_data = medida.get("data")
        medida_data = datetime.strptime(medida_data,"%d/%m/%Y %H:%M").date()
        
        if medida_data == datas:
            data_list.append(medida)
    if data_list == []:
        return jsonify({"error": "Data não encontrada"}), 404
    else:
        return jsonify(data_list)