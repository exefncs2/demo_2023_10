from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

# 指定存儲桶名稱、要下載的對象路徑，以及要將資料保存到的本地文件路徑
bucket_name = f"<bucket名稱>"
source_blob_name = f"<dir><filename>"
destination_file_name = f"<下載來檔案名稱>"

# 呼叫下載函數
download_blob(bucket_name, source_blob_name, destination_file_name)