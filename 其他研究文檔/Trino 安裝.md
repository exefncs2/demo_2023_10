# Trino 安裝
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

`docker pull trinodb/trino`
<br>

## 創建檔案(連線內容`為測試用，服務都已經開好)
* 基本設定檔:config.properties
<br>
```coordinator=true
node-scheduler.include-coordinator=true
http-server.http.port=8090
discovery-server.enabled=true
discovery.uri=http://localhost:8090
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
connection-url=jdbc:postgresql://<your_ip>:5432/<your_db>
connection-user=<user>
connection-password=<password>
```

* redshift設定檔Redshift/config.properties (已刪除資料庫但保留作法)
<br>
```connector.name=redshift
connection-url=jdbc:postgresql://<your_ip>:5439/base
connection-user=<user>
connection-password=<password>
```
### p.s. redshift使用連線為同伺服器docker內部連線用，需要先綁定內部網路，正常情況啟動後會有一個預設的內部網路

查看網路:<br>
`docker network inspect <your_network_name>`

新增連線:<br>
`docker network connect <your_network_name> <redshift容器名>`

<br><br>

* 整個docker的設定檔:docker-compose.yaml
<br>
```version: '3'
services:
  coordinator:
    image: trinodb/trino
    environment:
      - Trino_LOG_LEVEL=DEBUG
    ports:
      - "8090:8080" (這裡8080讓給presto所以用8090)
      - "5432:5432" (這邊如果有開共用網路可以只有一個容器寫就好)
    container_name: "coordinator_trino"
    volumes:
      - ./config.properties:/data/trino/etc/config.properties
      - ../PostgreSQL/config.properties:/data/trino/catalog/postgresql.properties (直接放etc會對容器內部設計造成衝突 add_etc隨便取的)
      - ../Redshift/config.properties:/data/trino//add_etc/catalog/redshift.properties (已刪除資料庫但保留作法)
    
```
### wranning: add_etc要進到容器內手搬回etc內因為內部bash不夠完整又不能修改，沒搬就沒有連線了，並且要重啟服務才能啟用。

### p.s. redshift的port沒有在裡面，因為使用的是內部網路

### p.s. Trino_LOG_LEVEL=DEBUG是測試用顯示可以用docker logs <容器名>查看內容

以上皆放在同個資料夾便可啟動
如果修改也都是修改這修檔案後重啟服務

## 指令啟動
啟動<br>
`docker compose up -d`

關閉(包含刪除)<br>
`docker compose down`

進入容器<br>
`docker exec <容器名> bash`

單體操作(只有修改文件建議)<br>

1. 先停止容器(如果exit錯誤不需要) <br> `docker stop <容器名>`

2. 刪除舊容器(只會刪除Trino本體worker與network保留)<br>`docker rm <容器名>`


3. 修改文件


4. 再啟動<br>`docker compose up -d`

## 連線方式
1. [官方下載](https://trino.io/download.html)驅動器

2.使用相應的連線這裡用[java檔](trino-cli-419-executable.jar)

3.開啟cmd執行<br>
`java -jar .\trino-cli-419-executable.jar --server <your_ip>:8090`

### p.s. 此為測試位置須以現實狀況考慮ip等

### Trino 沒有內建worker的概念所以要已多站點的方式互相串接一起