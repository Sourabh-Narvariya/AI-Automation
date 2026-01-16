# Create a Flask API that takes a number and returns its square via POST method.
import io
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/api/square', methods=['POST'])
def square_number():
    """Return the square of a given number"""
    data = request.get_json()
    if not data or 'number' not in data:
        return jsonify({"error": "Please provide a number"}), 400
    
    try:
        number = float(data['number'])
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400
    
    squared_value = number ** 2
    return jsonify({"number": number, "squared": squared_value}), 200
if __name__ == '__main__':
    app.run(debug=True)


