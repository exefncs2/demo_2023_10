Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### 補充文件:
可參考[建構文書](/read_file//DBT/demo/prefect_docker/demo/read_file/文書使用說明.md)的兩種
- elementary [詳細](/read_file//DBT/demo/prefect_docker/demo/read_file/文書使用說明.md)
- dbt_artifacts


### 基本table:
vars上有設定的table
  - myrow_data: 'row_data' >> row_data 拆分表能完整將json拆成碎片化使用
  - myschema: 'dbt' >> schema 名稱
  - myorigin: 'p_origin' >> 最基本的table 由bucket直接把資料灌入 只有兩個欄位 data(jsonb)放整個json檔 跟 insert_date(date)寫入日期


### 基本說明:
由FHIR轉OMOP，先由p_origin的data欄位為FHIR拆分成row_data然後用base_table_macros拆成不同類的總表(models/sources)在由OMOP表(models/staging)建構OMOP表
優點:全拆分有新欄位重跑時會自動帶入
缺點:可能OMOP有但FHIR沒有所以會帶入錯誤

此篇OMOP表並沒有完成但作為demo已能提供技術參考