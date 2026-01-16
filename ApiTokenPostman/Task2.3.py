# Task 3: Build GET, POST, PUT, DELETE Flask API and test it on Postman.
import io
import base64   
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
# In-memory data store
data_store = {}
@app.route('/api/items', methods=['GET'])
def get_items():
    """Get all items"""
    return jsonify(data_store)
@app.route('/api/items/<item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item"""
    item = data_store.get(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({item_id: item})
@app.route('/api/items', methods=['POST'])
def create_item():
    """Create a new item"""
    item = request.json
    item_id = str(len(data_store) + 1)
    data_store[item_id] = item
    return jsonify({item_id: item}), 201
@app.route('/api/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item"""
    if item_id not in data_store:
        return jsonify({"error": "Item not found"}), 404
    item = request.json
    data_store[item_id] = item
    return jsonify({item_id: item})
@app.route('/api/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item"""
    if item_id not in data_store:
        return jsonify({"error": "Item not found"}), 404
    del data_store[item_id]
    return jsonify({"message": "Item deleted"})
if __name__ == '__main__':
    app.run(debug=True)

