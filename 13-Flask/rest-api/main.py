from flask import Flask,jsonify, request

app = Flask(__name__)

items = [
    {
        'id': 1,
        'name': 'Luke'
    },
    {
        'id': 2,
        'name': 'Leah'
    }
]

@app.route("/items")
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>")
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    return jsonify(item)

@app.route("/items", methods=['POST'])
def create_item():
    
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Error occurred."})
    
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1 ,
        "name": request.json['name']
    }
    
    items.append(new_item)

    return jsonify(new_item)

@app.route("/items/<int:item_id>", methods=['PUT'])
def update_item(item_id):
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Error occurred"})
    
    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"})
    
    item['name'] = request.json.get('name', item['name'])
    return jsonify(item)

@app.route("/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    if not item_id:
        return jsonify({"error": "Error occurred"})
    global items
    items = [item for item in items if item['id'] != item_id]

    return jsonify({"result": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)