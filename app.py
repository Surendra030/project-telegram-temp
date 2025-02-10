import tempfile
import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from load_json import get_json_data
app = Flask(__name__)
CORS(app)

json_data = get_json_data()
url_data = json_data['url_data']

def get_mega_link(serial_num):
    for obj in url_data:
        serial = obj['serial_num']
        if serial == serial_num:
            return obj
    
    return "https://mega.nz/example-pdf-link.pdf"


@app.route('/')
def home():
    return jsonify({"message": "Backend server is running successfully"}), 200


@app.route("/process", methods=["POST"])
def process_request():
    data = request.get_json()
    
    if not data or "serial_number" not in data:
        return jsonify({"error": "No serial number provided"}), 400
    
    serial_number = data["serial_number"]
    obj = get_mega_link(serial_number)  # Call the function with serial number
    
    if obj is not None:
        return jsonify(obj)
    else:
        return jsonify({"error": "Failed to retrieve data"}), 500


if __name__ == "__main__":
    app.run(debug=True)
