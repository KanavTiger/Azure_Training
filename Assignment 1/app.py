from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)
blob_service_client = BlobServiceClient.from_connection_string("GetYourString")
container_name = "assignment-data"

@app.route('/list-files', methods=['GET'])
def list_files():
    folder = request.args.get('folder')
    container_client = blob_service_client.get_container_client(container_name)
    blob_list = container_client.list_blobs(name_starts_with=folder + "/")
    files = [blob.name for blob in blob_list]
    return jsonify(files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
