from google.cloud import vision
from flask import Flask, request, jsonify, render_template
import os
import base64
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Read the base64-encoded credentials from the encoded_credentials.txt file in binary mode
with open("encoded_credentials.txt", "rb") as file:
    credentials_base64 = file.read().strip()

if not credentials_base64:
    raise EnvironmentError("The encoded_credentials.txt file is empty or not found")

# Decode the base64-encoded credentials and write them to the original JSON file
credentials_json = base64.b64decode(credentials_base64)
with open("image-captioning-with-gemini-f5a9a8ab3cfb.json", "wb") as f:
    f.write(credentials_json)

# Set the environment variable to point to the newly created credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "image-captioning-with-gemini-f5a9a8ab3cfb.json"

# Initialize the Google Cloud Vision API client
client = vision.ImageAnnotatorClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # Process the image through Google Cloud Vision API
        image_content = file.read()
        image = vision.Image(content=image_content)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        tags = [label.description for label in labels]
        return jsonify({'message': 'File successfully uploaded', 'tags': tags}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
