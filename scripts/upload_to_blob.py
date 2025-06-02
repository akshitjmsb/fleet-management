from azure.storage.blob import BlobServiceClient

AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "ais-data"
BLOB_NAME = "fake_ais_data.csv"
LOCAL_FILE_PATH = "storage/fake_ais_data.csv"

def upload_blob():
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

    with open(LOCAL_FILE_PATH, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded {LOCAL_FILE_PATH} to Azure Blob Storage as {BLOB_NAME}")

if __name__ == "__main__":
    upload_blob()
