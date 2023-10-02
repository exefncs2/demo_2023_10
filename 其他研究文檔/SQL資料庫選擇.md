# SQL資料庫選擇
## 優先推薦
### MSSQL
優點:功能性最高，性能最好且GCP有內置啟動<br>
缺點:要收費

### greenplum/psql
優點:功能性優秀，使用簡單且免費，GCP也有psql內置啟動但greenplum需要人工配置<br>
缺點:沒有排程機能，greenplum機器不多的情況下效果一般
| 功能/特性     | psql                             | Greenplum                          |
| -------------- | -------------------------------- | ---------------------------------- |
| 資料庫類型     | 單節點                           | 分佈式                             |
| 並行查詢       | 支援                             | 支援                               |
| 資料分片       | 不支援                           | 支援                               |
| 資料壓縮       | 支援                             | 支援                               |
| 資料備份恢復   | 單節點                           | 分佈式                             |
| 資料分析功能   | 有                               | 更強大                             |

### MYSQL
不考慮，但GCP有內置啟動

## 特殊考量
### Cassandra
作為NOSQL但功能類似並且免費
雖然沒有join等等複雜功能也沒有sp
不過可以用python彌補一切

# NOSQL資料庫選擇
## 優先推薦
### Couchbase
優點:功能性最高，使用SQL語法最快捷便利學習<br>
缺點:有社區版跟企業版差別可能會需要企業版

## 適合推薦
### MongoDB
優點:基礎功能不錯，有較多文本<br>
缺點:取用資料query方式比較特別需要學習成本，安全性較低，也是有共享版與企業版差異

### Cassandra
優點:使用SQL語法最快捷便利學習<br>
缺點:與SQL模式太過相近缺乏便利度

### Neo4j 
優點:用節點的方式，在資料傳遞中較為快速<br>
缺點:取用資料query方式比較特別需要學習成本

# 排程工具選擇
### Apache Airflow
Airflow是一個開源的工作流程管理平台，可以用於建立、排程和監控工作流程。它支援Python和SQL，並提供豐富的功能和可擴展性。

### Celery
Celery是一個分散式任務隊列系統，可以用於異步任務的排程和執行。它支援Python，並提供豐富的功能，如任務狀態監控、任務重試、任務優先級等。

### Luigi
 Luigi是一個Python模塊，用於構建複雜的數據管道和工作流程。它提供了一個聲明式的方式來定義任務和依賴關係，並支援在排程器中執行這些任務。

### Apache Nifi
Nifi是一個開源的數據流程管理工具，可以用於構建和管理數據流程。它支援SQL和Python腳本，並提供可視化的界面和強大的數據轉換和處理能力。

### SQL Server Agent (推薦)
如果你使用的是Microsoft SQL Server，SQL Server Agent是一個內建的工作排程工具，可以用於排程SQL任務和作業。它支援T-SQL腳本和存儲過程，並提供計劃排程和警報功能。

以上推薦用sql本身去將python整理好的table做輸出，可以在SQL Server Agent的作業中使用"CmdExec"或"T-SQL"類型的步驟來執行Python腳本，唯一問題是要收費。


### 補充

| 工具             | Apache Airflow                                                    | Apache NiFi                                               |
|----------------|----------------------------------------------------------------|----------------------------------------------------------|
| 底層語言         | Python                                                           | Java                                                     |
| 任務導向         | Job oriented                                                     | Data oriented                                            |
| 核心處理單元     | Operators，除了 DB 類型之外，其他像是工作類型的服務也有支援 | Processors，只支援 DB、Message Queue等與資料相關的服務 |
| 能否取得上游資訊 | 不行，除非特別 push xcom，否則下游無法取得上游 operator 的資訊   | FlowFiles 本身就會帶著上游 Processor 產生的資訊到下游，所以後續的 Processor 都可以應用到上游的 metadata |
| Schedule       | 較偏向於 Batch 的操作                                              | 較適用於 Streaming 的操作                                        |


只要你的服務當中的 task 不太需要上游的資料且相互獨立時，或許 Airflow 會是一個較好的選擇; 反之，如果都需要從每一個地方讀取資料做處理，接著處理完再存回到另一個地方時，則 NiFi 就會是一個更適合的選擇。

來源：[iT邦幫忙 Day29 NiFi 與其他工具的比較 from Mars Su](https://ithelp.ithome.com.tw/articles/10281489)