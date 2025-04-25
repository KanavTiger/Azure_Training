from flask import Flask, request, jsonify
import joblib
import logging
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Azure Blob Storage Setup
blob_connection_string = "Get_Your_String"
container_name = "assignmnet-data-new"
model_filename = "house_price_model.pkl"
model = None

def load_model():
    """Function to load model from Azure Blob Storage."""
    global model
    if model is None:
        logger.info("Loading model from Azure Blob Storage...")
        blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(model_filename)

        with open("model.pkl", "wb") as f:
            f.write(blob_client.download_blob().readall())

        model = joblib.load("model.pkl")
        logger.info("Model loaded successfully.")

@app.before_first_request
def startup():
    """Flask startup to load the model only once."""
    load_model()

@app.route('/predict', methods=['POST'])
def predict():
    """Predict house price based on request input."""
    try:
        data = request.get_json()
        logger.info(f"Received request: {data}")

        input_features = [
            data['sqft'],
            data['bedrooms'],
            data['age'],
        ]

        prediction = model.predict([input_features])[0]

        logger.info(f"Prediction: {prediction}")
        return jsonify({"prediction": prediction})

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
