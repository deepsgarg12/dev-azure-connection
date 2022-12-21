import traceback

import pandas as pd
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
import logging
import os

logging.basicConfig(encoding='utf-8', level=logging.ERROR)

class storageConnector():
    _tenant_id = None
    _client_id = None
    _client_secret = None

    def __init__(self, tenant_id, client_id, client_secret):
        self._tenant_id = tenant_id
        self._client_id = client_id
        self._client_secret = client_secret

    def readBlobFromStorageAccount(self, storage_name: str, container_name: str, blob_name: str):
        # Replace with your service principal's client ID, tenant ID, and secret
        clientId = self._client_id
        # Replace with your service principal secret
        clientSecret = self._client_secret
        # Replace with your tenant ID
        tenantId = self._tenant_id
        # Use the credentials and account_url to authenticate with the edgevu account and create a client object
        access_key = ClientSecretCredential(tenantId, clientId, clientSecret)
        service_client = BlobServiceClient(credential=access_key, account_url=f"https://{storage_name}.blob.core.windows.net")
        logging.info("***********Connection has been established************")

        # Use the client to list the blobs in the container
        blob = service_client.get_container_client(container_name)

        try:
            with open(f"{blob_name}", "wb") as f:
                data = blob.download_blob(blob=blob_name)
                data.readinto(f)
        except Exception:
            traceback.print_exc()
            logging.error("***********Cannot read the blob*****************")

        df = pd.read_csv(f"{blob_name}")
        #remove the file
        os.remove(blob_name)
        return df


    def writeBlobIntoStorageAccount(self, storage_name: str, container_name: str, df, blob_name:str):
        # Replace with your service principal's client ID, tenant ID, and secret
        clientId = self._client_id
        # Replace with your service principal secret
        clientSecret = self._client_secret
        # Replace with your tenant ID
        tenantId = self._tenant_id
        # Use the credentials and account_url to authenticate with the edgevu account and create a client object
        access_key = ClientSecretCredential(tenantId, clientId, clientSecret)
        account_url = f"https://{storage_name}.blob.core.windows.net"
        service_client = BlobServiceClient(credential=access_key, account_url=account_url)
        logging.info("***********Connection has been established************")

        # Create a new blob
        blobname = blob_name
        blob = service_client.get_blob_client(container_name, blobname)

        # Write the DataFrame to a CSV file
        df.to_csv(blob_name, index=False)

        # Open the CSV file for reading in binary mode
        try:
            with open(blobname, "rb") as data:
                # Write the contents of the CSV file to the blob
                blob.upload_blob(data)
                logging.info("***********Dataframe has been written to the Storage account.*********")
        except Exception:
            logging.error("********Cannot write the dataframe into blob")
            traceback.print_exc()
        finally:
            #Remove the file
            os.remove(blobname)