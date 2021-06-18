from flask import jsonify
from application import app


@app.route("/", methods=['GET'])
def home():
    return 