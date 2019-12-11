import keras
import numpy as np
from keras.applications import mobilenet, mobilenet_v2
from keras.models import Model
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing import image
import os
import json
from PIL import Image
import io

mobilenet_model = mobilenet.MobileNet(weights='imagenet')
new_model = Model(mobilenet_model.inputs, mobilenet_model.layers[-6].output)
new_model._make_predict_function()

def prepare_image(file):
    """Resize image to 224x224 and preprocessing."""
    img = Image.open(io.BytesIO(file)).resize((224, 224))
    img_array = np.asarray(img)
    # Convert from (height, width, channels) to (no. of samples, height, width, channels)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

def encode_image(file):
    """Generate embeddings for image."""
    preprocessed_image = prepare_image(file)
    predictions = new_model.predict(preprocessed_image)
    return predictions.reshape(1024)

def load_encoding(path):
    """Load embeddings of shirts collection."""
    with open(path, 'r') as f:
        data_encoding = f.read()
    return json.loads(data_encoding)

def getCS(encoding1, encoding2):
    """Compute cosine similarity between two embeddings."""
    return np.dot(encoding1, np.array(encoding2))/(np.linalg.norm(encoding1)*np.linalg.norm(np.array(encoding2)))

# Load shirt encodings
shirt_encoding_map = load_encoding('/home/site/wwwroot/ShirtSim/shirt_encoding.txt')

def find_similar(test_image_file, threshold=0.7):
    """Given a image, find the most similar shirt and its similarity score that is above the threshold."""
    test_img_encoding = encode_image(test_image_file)
    keys = list(shirt_encoding_map.keys())
    vals = list(shirt_encoding_map.values())
    sim_arr = list(map(lambda x: getCS(test_img_encoding, x), vals))
    idx = np.argmax(sim_arr)
    if sim_arr[idx] < threshold:
        return None, None
    tag = keys[idx]
    return tag, sim_arr[idx]
