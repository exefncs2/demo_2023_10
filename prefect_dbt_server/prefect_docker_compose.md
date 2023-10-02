# 資料庫外接版

## docker compose
使用[prefect_docker]

### 裝置指令
```
docker compose up --build -d
```

### 解除指令
```
docker compose down -v
```

## 過程
1. 建立postgres並創好db跟帳號
2. 啟動prefect服務並使用創立好的postgres放置內部table這(原本使用預設的sqllite但這很危險，可能會滿了並且sqllite不能併發而產生異常)
3. 至網頁UI上手動加入GCP認證的block不過這也是保障安全
4. 進入容器內加入工作已濃縮成一個main.py可執行