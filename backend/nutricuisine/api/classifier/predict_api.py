from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename

from nutricuisine.api.classifier.utils import classify_image

predict_blueprint = Blueprint('predict', __name__, url_prefix='/predict')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@predict_blueprint.post('/')
def predict_root(): 
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        file.save(img_path)

        try:
            result = classify_image('FV.h5', 'labels.json', img_path)
            os.remove(img_path)
            return jsonify({'result': result}), 200
        except Exception as e:
            os.remove(img_path)
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400
