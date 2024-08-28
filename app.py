from google.cloud import vision
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not credentials_path:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")

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
