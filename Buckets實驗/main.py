
from fastapi import FastAPI  , File, UploadFile
from google.cloud import storage
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
google_auth = '<credentials-key.json>' # 認證json path


@app.post("/upload")
async def upload_file(dir: str, file: UploadFile = File(...)):
    bucket_name = f"<bucket_name>" # bucket的名字
    upload_to_gcs(file.file, bucket_name, f'{dir}/{file.filename}')
    
    return {"message": "File uploaded successfully."}

def upload_to_gcs(file, bucket_name, destination_blob_name):
    storage_client = storage.Client.from_service_account_json(google_auth)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(file)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
