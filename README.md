# Directory structure
```bash
edgevu-storageconnector
|   README.md
|   requirements.txt
|   setup.py 
+---edgevu
|   |   connectors.py
|   |   __init__.py
```
```Note```: Any new script is going to be inside the edgevu_storageconnector. 

## Installing
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```

```Note```: If still showing error pip3 is not recognizable, try to configure pip/pip3 in environment varialbles.

## Usage
### This is Azure storage connector which will help to connect with the storage account to read and write the blob.

We have a class called storageConnector which takes three parameters called Client id, Tenant id, Client Secret. We are storing keys in the key vault and accessing the secret keys.

##### obj = storageConnector(client_id,client_secret,tenant_id)

#### Once connected we will read the blob from the storage account by using readBlobFromStorageAccount function. This function takes three parameters i.e. name of storage account, name of container and the blob which you want to read.
e.g:
##### df = obj.readBlobFromStorageAccount(storage_name, container_name, blob_name)

#### We can also write the dataframe into storage account as a blob into storage account by using writeBlobIntoStorageAccount function. This function takes fours paramaters i.e. dataframe, storage name, container name and the name of the blob 

e.g:
##### obj.writeBlobIntoStorageAccount(storage_name, container_name, blob_name, df)
