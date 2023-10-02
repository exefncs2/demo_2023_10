# PRESTO 安裝
## docker
先安裝 docker 完整功能<br>

 更新機器<br>
`sudo apt update`
<br>

安裝
<br>
`sudo apt install docker`


## install
裝上最新的image<br>

`docker pull ahanaio/prestodb-sandbox`
<br>

## 創建檔案(連線內容`為測試用，服務都已經開好)
* 基本設定檔:config.properties
<br>
```coordinator=true
node-scheduler.include-coordinator=true
http-server.http.port=8080
discovery-server.enabled=true
discovery.uri=http://localhost:8080
```

* worker設定檔:worker/config.properties
<br>
```coordinator=false
http-server.http.port=8083
discovery.uri=http://coordinator:8080
```
### p.s. 這裡只用一個但worker可以多個使用
<br><br>

* PSQL設定檔:PostgreSQL/config.properties
<br>
```connector.name=postgresql
connection-url=jdbc:postgresql://<yourIP>:5432/<your_db>
connection-user=<user>
connection-password=<password>
```

* redshift設定檔Redshift/config.properties (已刪除資料庫但保留作法)
<br>
```connector.name=redshift
connection-url=jdbc:postgresql://<yourIP>:5439/<your_db>
connection-user=<user>
connection-password=<password>
```
### p.s. redshift使用連線為同伺服器docker內部連線用，需要先綁定內部網路，正常情況啟動後會有一個預設的內部網路

查看網路:<br>
`docker network inspect <network_name>`

新增連線:<br>
`docker network connect <network_name> <redshift容器名>`

<br><br>

* 整個docker的設定檔:docker-compose.yaml
<br>
```version: '3'
services:
  coordinator:
    image: ahanaio/prestodb-sandbox
    environment:
      - PRESTO_LOG_LEVEL=DEBUG
    ports:
      - "8080:8080"
      - "5432:5432"
    container_name: "coordinator"
    volumes:
      - ./config.properties:/opt/presto-server/etc/config.properties
      - ../PostgreSQL/config.properties:/opt/presto-server/etc/catalog/postgresql.properties
      - ../Redshift/config.properties:/opt/presto-server/etc/catalog/redshift.properties (已刪除資料庫但保留作法)
    
  worker:
    image: ahanaio/prestodb-sandbox
    container_name: "worker0"
    ports:
      - "8083:8083"
    volumes:
      - ./worker/config.properties:/opt/presto-server/etc/config.properties
    depends_on:
      - coordinator
```
### p.s. redshift的port沒有在裡面，因為使用的是內部網路

### p.s. PRESTO_LOG_LEVEL=DEBUG是測試用顯示可以用docker logs <容器名>查看內容

以上皆放在同個資料夾便可啟動
如果修改也都是修改這修檔案後重啟服務

## 指令啟動
啟動<br>
`docker compose up -d`

關閉(包含刪除)<br>
`docker compose down`

單體操作(只有修改文件建議)<br>

1. 先停止容器(如果exit錯誤不需要) <br> `docker stop <容器名>`

2. 刪除舊容器(只會刪除presto本體worker與network保留)<br>`docker rm <容器名>`


3. 修改文件


4. 再啟動<br>`docker compose up -d`

## 連線方式
1. [官方下載](https://prestodb.io/getting-started.html)驅動器

2.使用相應的連線這裡用[java檔](presto-cli-0.281-executable.jar)

3.開啟cmd執行<br>
`java -jar .\presto-cli-0.281-executable.jar --server 104.199.144.45:8080`

### p.s. 此為測試位置須以現實狀況考慮ip等