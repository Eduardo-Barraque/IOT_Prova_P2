from flask import jsonify, request
from application.model.entity.detector import Poluicao
from application.model.dao.detectores_dao import Detector_dao
from datetime import datetime, date 
import json
from application import app

detectores_list = Detector_dao().resultados_list()

@app.route("/valores", methods=['GET'])
def home():
    with open('dados.json', 'r') as var:
        dados_json = json.load(var)
        
    with open('dados.json', 'w') as var:
        json.dump(dados_json, var)   
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
    detectores_list.append(new_detector)
    return new_detector.toJson(), 201


@app.route("/valores/id/<id>", methods=['GET'])
def view_valor(id):
    view_list = []
    for medida in detectores_list:
        if medida.id == id:
            view_list.append(medida)
    if view_list == []:
        return jsonify({"error": "Medicao não encontrada"}), 404
    else:
        dados_view = [dado.toJson() for dado in view_list ]
        return jsonify(dados_view)


@app.route("/valores/data/<datas>", methods=['GET'])
def view_data(datas):
    data_list = []
    for medida in detectores_list:
        medida_data = date.strftime(medida.data,'%d-%m-%Y')
        if medida_data == datas:
            data_list.append(medida)
    if data_list == []:
        return jsonify({"error": "Data não encontrada"}), 404
    else:
        data_view = [dado.toJson() for dado in data_list ]
        return jsonify(data_view)