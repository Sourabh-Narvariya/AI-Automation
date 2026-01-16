# Task 2: Use Postman to send a POST request with JSON data to your local Flask app.
# Simple Flask API that accepts JSON via POST and echoes a response.
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/echo", methods=["POST"])
def echo_json():
	payload = request.get_json(silent=True) or {}
	if not payload:
		return jsonify({"error": "No JSON payload received"}), 400

	name = payload.get("name", "friend")
	return jsonify({"message": f"Hello, {name}!", "received": payload}), 200


if __name__ == "__main__":
	app.run(debug=True)