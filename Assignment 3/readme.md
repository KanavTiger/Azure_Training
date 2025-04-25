# House Price Prediction Flask API - Docker Deployment
This project demonstrates how to deploy the House Price Prediction Flask API using Docker. The Flask app is containerized, allowing it to run consistently across different environments.

## Prerequisites
* Docker installed on your machine.

## Steps to Deploy

### Clone the repository
    `cd /Github/azure_training`
    `git clone https://github.com/KanavTiger/mle-training/tree/main/Assignment5/5.2%20housing-price-prediction/housing-price-prediction.git`

### Dockerfile
 The project contains a *Dockerfile* that builds a Docker image for the Flask app. The Dockerfile does the following:
    * Uses a Python base image.
    * Copies the app files into the container.
    * Installs the necessary Python dependencies.
    * Exposes port 5000 for Flask.
    * Uses Gunicorn to serve the Flask app.

### 3. Build the Docker Image
To build the Docker image, run the following command:
`docker build -t flask-app` .

### 4. Run the Docker Container:
After building the image, you can run the container with:
`docker run -p 5000:5000 flask-app`

## Azure Blob Storage Setup
1. Create a Blob Storage Container:
    * Create an Azure Blob Storage account.
    * Create a container (*assignmnet-data-new*) to store the trained model file.

2. Upload the Model:
    * Upload your model file (*house_price_model.pkl*) to the created container.

3. Connection String:
    * Obtain the Azure Blob Storage connection string from the Azure portal.
    * Update the *blob_connection_string* variable in *app.py* with the correct connection string.


Let me know if you need any adjustments or additional details! This README provides basic information on setting up, running, and testing the Flask app, as well as how the Docker setup work