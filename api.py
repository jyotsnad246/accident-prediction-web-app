from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

# Load the saved TensorFlow Keras model
model = tf.keras.models.load_model("models/mymodel.h5")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    year = data["year"]
    month = data["month"]
    input_data = np.array([[0, 0, year, month]])  # Replace the 2s with the appropriate values for category and accident type

    prediction = model.predict(input_data)[0]

    response = {"prediction": float(prediction)}
    return jsonify(response), 200, {"Content-Type": "application/json"}

if __name__ == "__main__":
    app.run()
