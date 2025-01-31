import tempfile
import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from img_to_drawing import fetch_sketch

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Backend server is running successfully"}), 200

@app.route("/process", methods=["POST"])
def process_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        # Create a temporary directory for storing the image
        with tempfile.TemporaryDirectory() as temp_dir:
            # Define input and output image file paths in the temporary directory
            input_img_path = os.path.join(temp_dir, "img.png")
            output_img_path = os.path.join(temp_dir, "output.png")
            default_img_path = "default.png"  # Make sure default.png is available in the working directory

            # Save uploaded image to the temporary directory
            file = request.files["image"]
            file.save(input_img_path)

            # Process the image
            if fetch_sketch(input_img_path, output_img_path):
                return send_file(output_img_path, mimetype="image/png")
            else:
                return send_file(default_img_path, mimetype="image/png")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
