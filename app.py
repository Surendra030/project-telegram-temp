import tempfile
import os
from flask import Flask, request, send_file,jsonify
from flask_cors import CORS
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Backend server is running successfully"}), 200



@app.route("/process", methods=["POST"])
def process_image():
    if "image" not in request.files:
        return {"error": "No image uploaded"}, 400

    # Use a temporary directory instead of 'uploads'
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_filename = tmp_file.name
        file = request.files["image"]
        file.save(tmp_filename)

        # Process the image (for example, returning the same file)
        return send_file(tmp_filename, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)

