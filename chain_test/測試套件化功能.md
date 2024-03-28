# 套件需求

## 功能

1. **DB連線認證**: 確保安全地連接至數據庫。
2. **GCP連線認證**: 設定與Google Cloud Platform的安全連接。
3. **ChatGPT連線認證**: 實現與ChatGPT API的安全認證連接。
4. **Chunk方法(統一)**: 提供一致的資料分割處理方法。
5. **Embeddings方法(統一)**: 提供一致的數據嵌入處理方法。
6. **輸入資料處理**: 根據來源統一或根據GL/CL切分方法（如：`inputGL`, `inputCL`）。
7. **輸出資料處理**: 統一格式輸出或根據GL/CL切分方法（如：`outputGL`, `outputCL`）。
8. **Log記錄**: 實現統一的日誌記錄機制。
9. **專用密鑰公式**: 管理與使用專用的加密密鑰。
10. **`.env`專用讀取**: 實現`.env`文件的讀取，支持預設或本地配置。

## 問題

1. **OpenAI成本**: OpenAI使用可能涉及成本問題。
2. **連線權限需求**: 與外部系統連線時需要相應的權限設置。

## 結構

```plaintext

├── rag_chain
│   ├── __init__.py
│   ├── pyproject.toml
│   └── src
│       └── rag_chain
│           ├── core
│           │   ├── config.py
│           │   └── __init__.py
│           ├── db
│           │   ├── database.py
│           │   ├── __init__.py
│           │   ├── models.py
│           │   ├── operations.py
│           │   └── session.py
│           ├── gcp_integration
│           │   ├── __init__.py
│           │   └── secrets.py
│           ├── openai_integration
│           │   ├── embeddings.py
│           │   ├── __init__.py
│           │   └── openai_client.py
│           ├── text_processing
│           │   ├── chunking.py
│           │   └── __init__.py
│           └── utils
│               ├── __init__.py
│               └── logging_utils.py
```

### 安裝
``` 
pip install -e <until path>
```

### 啟動
- 測試的main (test_api)
	- 啟動: uvicorn app.main:app --reload --host 0.0.0.0 --port <port>
	- GCP proxy: gcloud compute start-iap-tunnel <GCP機器名稱> <port> --local-host-port=localhost:<port> --project <GCP專案名>
	- 瀏覽器連線: http://127.0.0.1:<port>/docs