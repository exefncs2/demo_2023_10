# redshift測試結果

## 測試結果
使用VM安裝docker image [guildeducation/docker-amazon-redshift](https://hub.docker.com/r/guildeducation/docker-amazon-redshift)
經過一番設定
發現他跟psql兼容極高 甚至自己的連接套件(python、JDBC)都不能連線 使用psql的反而成功

### 錯誤
參數錯誤，套件有一些預設參數強制輸入但新版本已經沒有這些參數導致錯誤<br>
DBeaver(JDBC):<br>
FATAL: unrecognized configuration parameter "driver_version"

python:<br>
redshift_connector.error.ProgrammingError: {'S': 'FATAL', 'C': '42704', 'M': 'unrecognized configuration parameter "application_name"', 'F': 'guc.c', 'L': '3275', 'R': 'set_config_option'}

皆是有錯誤傳入參數導致


## 差異列表

| 功能/特性   | Redshift                                      | PSQL (PostgreSQL)                             |
|-------------|-----------------------------------------------|-----------------------------------------------|
| 數據庫引擎   | 基於 ParAccel 的雲數據倉儲解決方案              | 開源的關聯型資料庫管理系統                        |
| 分佈式架構   | 支援並行查詢和分佈式計算                          | 支援單機和分佈式架構                              |
| 儲存優化     | 针對大規模數據倉儲的高性能儲存和查詢優化            | 面向一般用途的資料庫引擎                          |
| 擴展性       | 可自動擴展儲存容量和計算資源                      | 需要手動配置和管理擴展性                            |
| 列存儲       | 使用列存儲進行高效數據壓縮和查詢                    | 默認使用行存儲                                    |
| 並發連接數   | 支援高並發連接數                                 | 支援適中的並發連接數                              |
| 數據加載和導出 | 支援使用 COPY 命令進行高速數據加載和導出            | 使用標準 SQL INSERT 和 COPY 命令進行數據加載和導出   |
| 數據複製     | 支援數據複製和高可用性                            | 支援數據複製和高可用性                              |
| 查詢性能     | 針對大規模數據倉儲和分析查詢進行優化                | 針對一般事務處理和查詢進行優化                        |
| 索引         | 僅支援主鍵和排序鍵索引                            | 支援更廣泛的索引類型，如 B 樹索引、哈希索引、全文索引等 |
| 用戶定義函數 | 有限支援用戶定義函數（UDF）                       | 支援廣泛的用戶定義函數（UDF）                        |
| 數據類型     | 與 PostgreSQL 大部分數據類型兼容                  | 支援廣泛的數據類型                                  |
| 系統表和視圖 | 部分系統表和視圖與 PostgreSQL 不兼容               | 與 PostgreSQL 兼容的系統表和視圖                     |
