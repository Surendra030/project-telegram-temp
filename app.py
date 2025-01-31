from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
from bson.json_util import dumps
import os
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/process", methods=["POST"])
def process_image():
    if "image" not in request.files:
        return {"error": "No image uploaded"}, 400
    
    file = request.files["image"]
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    return send_file(filename, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
