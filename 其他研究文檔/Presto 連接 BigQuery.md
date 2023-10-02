# Presto 連接 BigQuery

## 第一步 google帳戶管理介面
* 要先到 google GCP 管理介面
* IAM與管理>服務帳戶>金鑰
* 新增一筆選輸出json 或 匯入一筆
* 並且下載json檔


## 第二步 將檔案放在Presto機器中
* credentials-key.json為下載的json

* 建立 ../BigQuery/config.properties 
```
connector.name=bigquery
bigquery.project-id=<project-id>
bigquery.credentials-file=/opt/presto-server/etc/credentials-key.json
bigquery.views-enabled=true
```
p.s. bigquery.views-enabled=true 是讓view也能讀取
除了MATERIALIZED_VIEW

docker增加的
``` 
volumes:
    ...
      - ../BigQuery/config.properties:/opt/presto-server/etc/catalog/bigquery.properties
      - ../BigQuery/credentials-key.json:/opt/presto-server/etc/credentials-key.json  
      ...
```

將兩個檔案掛到docker內就完成了

