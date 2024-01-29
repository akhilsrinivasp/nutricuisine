from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import json
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# Load the model and labels from files
def load_model_and_labels(model_path, labels_path):
    model_path = os.path.join(path, model_path)
    labels_path = os.path.join(path, labels_path)
    try:
        model = load_model(model_path)
        with open(labels_path, 'r') as file:
            labels = json.load(file)
        return model, labels
    except Exception as e:
        print(f"Error loading model or labels: {e}")
        return None, None

# Prepare the image for prediction
def prepare_image(img_path, target_size=(224, 224, 3)):
    try:
        img = load_img(img_path, target_size=target_size)
        img = img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        return img
    except Exception as e:
        print(f"Error preparing image: {e}")
        return None

# Predict the class of the image
def predict_class(model, img, labels):
    try:
        prediction = model.predict(img)
        y_class = prediction.argmax(axis=-1)
        class_id = int(y_class[0])
        class_name = labels.get(str(class_id), "Unknown")
        return class_name.capitalize()
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Prediction error"

# Main function to run the prediction
def classify_image(model_path, labels_path, img_path):
    model, labels = load_model_and_labels(model_path, labels_path)
    if model is None or labels is None:
        return "Model or labels not loaded properly."
    
    img_path = os.path.join(path, img_path)
    img = prepare_image(img_path)
    if img is None:
        return "Image not prepared properly."
    
    prediction = predict_class(model, img, labels)
    return prediction

if __name__ == "__main__":
    model_path = "model.h5"
    labels_path = "labels.json"
    img_path = "/Users/akhilsp/Downloads/Tomato.jpg"
    prediction = classify_image(model_path, labels_path, img_path)
    print(prediction)