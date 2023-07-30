import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
import os
# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Function to get predictions based on input data
def get_predictions(input_data):
    model_path = os.path.join(current_dir, "models", "mymodel.h5")
    model = tf.keras.models.load_model(model_path)
    prediction = model.predict(input_data)
    return int(prediction[0])

# Flask web app
app = Flask(__name__)

# API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    year = data['year']
    month = data['month']

    # Formatting input values
    en_cat = 2
    en_type = 2

    # Create input data
    input_data = [[en_cat, en_type, int(year), int(month)]]
    input_data = np.array(input_data)

    # Get predictions
    prediction_value = get_predictions(input_data)

    # Return the predictions in JSON format
    return jsonify({"prediction": prediction_value})

# Run the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
