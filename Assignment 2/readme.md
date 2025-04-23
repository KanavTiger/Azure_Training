# House Price Prediction Flask API
This repository contains a Flask-based API for house price prediction. The model is loaded from Azure Blob Storage and is used to predict house prices based on input features. The API exposes a `/predict` endpoint that accepts POST requests with input data and returns a predicted house price.

## Features
    * Loads the house price prediction model from Azure Blob Storage.
    * Provides a RESTful API endpoint (/predict) for making predictions based on input data.
    * Logs incoming requests and predictions for traceability.
    * Can be deployed locally and tested with a REST client like Postman or Insomnia.

## Clone the repository
    `cd /Github/azure_training`
    `git clone https://github.com/KanavTiger/mle-training/tree/main/Assignment5/5.2%20housing-price-prediction/housing-price-prediction.git`

## Azure Blob Storage Setup
1. Create a Blob Storage Container:
    * Create an Azure Blob Storage account.
    * Create a container (*assignmnet-data-new*) to store the trained model file.

2. Upload the Model:
    * Upload your model file (*house_price_model.pkl*) to the created container.

3. Connection String:
    * Obtain the Azure Blob Storage connection string from the Azure portal.
    * Update the *blob_connection_string* variable in *app.py* with the correct connection string.

## Code Structure:
Here is the structure of files:
    * **app.py:** The main Flask app file that contains the logic for loading the model, the prediction endpoint, and logging.
    * **requirements.txt:** The list of Python packages required to run the app.
    * **README.md:** This file, which provides instructions on how to set up and use the app.


## Important Notes

* The prediction model (house_price_model.pkl) must be available in the Azure Blob Storage container for the app to load it. Make sure the model is updated when retraining is done.
* Make sure to manage the Azure Blob Storage connection string securely (don't hard-code it in the app for production environments).
* This app uses a basic logging setup. For production, consider integrating with services like Azure Monitor or similar for better logging management.