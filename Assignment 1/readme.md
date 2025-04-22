# Azure Blob Explorer - Flask App
The project demonstrates the use of **Microsoft Azure Cloud Services**  to build a cloud-native Python Flask application that connects to **Azure Blob Storage**, lists the files inside a folder, and serves this data via an API endpoint

## Task Overview
1. Resource Group Setup
    * Created a resource group: cloud_training in the East US region.

2. Storage Account and Blob Container
    * Provisioned a Storage Account in East US.
    * Created a Blob container with 3 folders (folder1, folder2, folder3).
    * Uploaded sample files to each folder.

3. Flask App Development
    * Built a Flask application that takes a folder name and lists the files inside it.
    * Integrated Azure SDK (azure-storage-blob) to connect to blob storage.

4. Virtual Network
    * Created a VNet with a subnet in East US.

5. App Deployment
    * Deployed the Flask app to the VM.
    * Configured systemd for persistent background running of Flask app.

6. Security
    * Restricted inbound VM access to IPs coming only through Tiger VPN (simulated by IP filtering via NSG).

7. Cost Management
    * Applied tags to resources for billing.
    * Retrieved cost breakdown for the cloud_training resource group.

8. Version Control and Collaboration
    * Created a feature branch and pushed code with detailed commits.
    * Submitted a Pull Request including the deployed app's public URL.

9. Cleanup
    * All Azure resources created for this assignment were deleted to avoid incurring charges.


## Project Structure
```
flask_blob_app
├── app.py                  # Main Flask application
├── README.md               # This documentation
├── azure_bill.png  # Screenshot of Azure billing
```

##  API Usage
Get list of files in a Folder

GET http://127.0.0.1:5000//list_files/

## Billing info
A screenshot of the billing data filtered using the appropriate tags has been added as azure_bill.png.

## Cleanup
To avoid unnecessary charges, all the Azure resources created (storage account, container, VM, VNet, etc.) were deleted post validation.

