from flask import Flask, request, jsonify
from donut_controller import DonutController

app = Flask(__name__) # Web App Server

donutController = DonutController()

@app.route('/') # Route or Endpoint
def index():
    return 'Hello, World!'

@app.route('/api/donuts', methods=['GET']) # added a new route or endpoint
def get_donuts():
    flavor = request.args.get('flavor', None) # http://127.0.0.1/api/donuts?flavor=chocolate
    result_donuts = donutController.get_donuts(flavor)
    return jsonify({"result": result_donuts}), 200

@app.route('/api/donuts', methods=['POST']) # added a new route or endpoint
def create_donuts():
    required_fields = ["name", "flavor", "price"]
    json_request = request.get_json()

    for field in required_fields:
        if not json_request.get(field, None):
            return jsonify({"error": "Missing required fields"}), 400
        
    result_donut = donutController.add_donut(
        json_request["name"],
        json_request["flavor"],
        json_request["price"]
    )

    return jsonify({"result": result_donut}), 201

@app.route('/api/donuts/<int:donut_id>', methods=['PUT'])
def update_donut(donut_id):
    required_fields = ["name", "flavor", "price"]
    json_request = request.get_json()

    for field in required_fields:
        if not json_request.get(field, None):
            return jsonify({"error": "Missing required fields"}), 400
        
    result_donut = donutController.update_donut(
        donut_id,
        json_request["name"],
        json_request["flavor"],
        json_request["price"]
    )

    if not result_donut:
        return jsonify({"error": "Donut with id {} does not exist.".format(donut_id)}), 404
    
    return jsonify({"result": result_donut}), 200

@app.route('/api/donuts/<int:donut_id>', methods=['DELETE'])
def delete_donut(donut_id):
    result = donutController.delete_donut(donut_id)

    if not result:
        return jsonify({"error": "Donut with id {} does not exist.".format(donut_id)}), 404
    
    return jsonify({"result": 'success'}), 200