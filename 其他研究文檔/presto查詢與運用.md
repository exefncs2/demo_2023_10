# 查詢
以bigquery來作範例:<br>

查catalogs<br>
SHOW CATALOGS;<br>

翻看bigquery下的schemas(dataset)<br>
SHOW SCHEMAS from bigquery;<br>

翻看dataform下面所有table<br>
SHOW TABLES from bigquery.dataform;<br>

查看特定table的所有欄位<br>
SHOW COLUMNS from bigquery.dataform."fhir_patients_view";<br>
<br>
顯示如[圖1](show_1.jpg)、[圖2](show_2.jpg)


<br>

# python連接

### 安裝專用套件
pip install 'pyhive[presto]'

### 語法
```
#示範用程式
from pyhive import presto

# 创建Presto连接
conn = presto.connect(
    host='127.0.0.1',
    port=8080
)

# 执行查询
query1 = "SHOW CATALOGS"
query2 = "SHOW SCHEMAS from bigquery"
query3 = "SHOW TABLES from bigquery.dataform"
query4 = "SHOW COLUMNS from bigquery.dataform.fhir_patients_view"

# 創建Presto游標
cursor = conn.cursor()

cursor.execute(query1)
results1 = cursor.fetchall()

# 处理查询结果
print('-----------CATALOGS--------------')
for row1 in results1:
   print(row1)
   
cursor.execute(query2)
results2 = cursor.fetchall()
print('-----------SCHEMAS--------------')
for row2 in results2:
   print(row2)
   
cursor.execute(query3)
results3 = cursor.fetchall()
print('-----------TABLES--------------')
for row3 in results3:
   print(row3)

cursor.execute(query4)   
results4 = cursor.fetchall()
print('-----------COLUMNS--------------')
for row4 in results4:
   print(row4)


# 关闭连接
conn.close()
```


## 內建API回傳 <br>
### 指令
``` curl -i -X POST   -H "Content-Type: application/json"   -H "X-Presto-User: felix"   -H "X-Presto-Set-Session: session_property=value"   -H "X-Presto-Set-Catalog: bigquery"   -H "X-Presto-Set-Schema: dataform"   --data 'SHOW COLUMNS FROM bigquery.dataform."fhir_patients_view"'   http://localhost:8080/v1/statement ```

### 回傳結果
```
HTTP/1.1 200 OK
Date: Tue, 27 Jun 2023 07:53:12 GMT
Content-Type: application/json
X-Content-Type-Options: nosniff
Content-Length: 687

{"id":"20230627_075312_00023_57rby","infoUri":"http://localhost:8080/ui/query.html?20230627_075312_00023_57rby","nextUri":"http://localhost:8080/v1/statement/queued/20230627_075312_00023_57rby/1?slug=xa51277643a46456dabec46a400558813","stats":{"state":"WAITING_FOR_PREREQUISITES","waitingForPrerequisites":true,"queued":false,"scheduled":false,"nodes":0,"totalSplits":0,"queuedSplits":0,"runningSplits":0,"completedSplits":0,"cpuTimeMillis":0,"wallTimeMillis":0,"waitingForPrerequisitesTimeMillis":0,"queuedTimeMillis":0,"elapsedTimeMillis":0,"processedRows":0,"processedBytes":0,"peakMemoryBytes":0,"peakTotalMemoryBytes":0,"peakTaskTotalMemoryBytes":0,"spilledBytes":0},"warnings":[]}
```

### 想看結果就把回傳 資訊的nextUri再打一次

```
curl -i -X GET http://localhost:8080/v1/statement/queued/20230627_075312_00023_57rby/1?slug=xa51277643a46456dabec46a400558813
```

### 結果
```
{
  "id": "20230627_075312_00023_57rby",
  "infoUri": "http://localhost:8080/ui/query.html?20230627_075312_00023_57rby",
  "columns": [
    {
      "name": "Column",
      "type": "varchar",
      "typeSignature": {
        "rawType": "varchar",
        "typeArguments": [],
        "literalArguments": [],
        "arguments": [
          {
            "kind": "LONG_LITERAL",
            "value": 2147483647
          }
        ]
      }
    },
    {
      "name": "Type",
      "type": "varchar",
      "typeSignature": {
        "rawType": "varchar",
        "typeArguments": [],
        "literalArguments": [],
        "arguments": [
          {
            "kind": "LONG_LITERAL",
            "value": 2147483647
          }
        ]
      }
    },
    {
      "name": "Extra",
      "type": "varchar",
      "typeSignature": {
        "rawType": "varchar",
        "typeArguments": [],
        "literalArguments": [],
        "arguments": [
          {
            "kind": "LONG_LITERAL",
            "value": 2147483647
          }
        ]
      }
    },
    {
      "name": "Comment",
      "type": "varchar",
      "typeSignature": {
        "rawType": "varchar",
        "typeArguments": [],
        "literalArguments": [],
        "arguments": [
          {
            "kind": "LONG_LITERAL",
            "value": 2147483647
          }
        ]
      }
    }
  ],
  "data": [
    ["fullurl", "varchar", "", ""],
    ["resource_resourcetype", "varchar", "", ""],
    ["id", "varchar", "", ""],
    ["resource_meta_versionid", "bigint", "", ""],
    ["resource_meta_lastupdated", "timestamp with time zone", "", ""],
    ["resource_meta_source", "varchar", "", ""],
    ["resource_text_status", "varchar", "", ""],
    ["resource_identifier", "varchar", "", ""],
    ["resource_gender", "varchar", "", ""],
    ["resource_birthdate", "date", "", ""],
    ["search_mode", "varchar", "", ""],
    ["resource_name", "varchar", "", ""],
    ["resource_managingorganization_reference", "varchar", "", ""],
    ["resource_telecom", "varchar", "", ""],
    ["resource_address", "varchar", "", ""],
    ["resource_contact", "varchar", "", ""],
    ["resource_extension", "varchar", "", ""],
    ["resource__birthdate_extension", "varchar", "", ""],
    ["resource_deceaseddatetime", "timestamp with time zone", "", ""],
    ["resource__deceaseddatetime_extension", "varchar", "", ""],
    ["resource_generalpractitioner", "varchar", "", ""],
    ["resource_maritalstatus_text", "varchar", "", ""],
    ["resource_active", "boolean", "", ""],
    ["resource_deceasedboolean", "boolean", "", ""],
    ["resource_managingorganization_type", "varchar", "", ""],
    ["resource_meta_profile", "varchar", "", ""],
    ["resource_managingorganization_displaydisplay", "varchar", "", ""],
    ["resource_maritalstatus_codingcodes", "varchar", "", ""],
    ["patientid", "varchar", "", ""]
  ],
  "stats": {
    "state": "FINISHED",
    "waitingForPrerequisites": false,
    "queued": false,
    "scheduled": true,
    "nodes": 1,
    "totalSplits": 19,
    "queuedSplits": 0,
    "runningSplits": 0,
    "completedSplits": 19,
    "cpuTimeMillis": 23,
    "wallTimeMillis": 485,
    "waitingForPrerequisitesTimeMillis": 22,
    "queuedTimeMillis": 0,
    "elapsedTimeMillis": 44328,
    "processedRows": 29,
    "processedBytes": 2744,
    "peakMemoryBytes": 0,
    "peakTotalMemoryBytes": 1538,
    "peakTaskTotalMemoryBytes": 1538,
    "spilledBytes": 0,
    "rootStage": {
      "stageId": "0",
      "state": "FINISHED",
      "done": true,
      "nodes": 1,
      "totalSplits": 1,
      "queuedSplits": 0,
      "runningSplits": 0,
      "completedSplits": 1,
      "cpuTimeMillis": 2,
      "wallTimeMillis": 10,
      "processedRows": 29,
      "processedBytes": 1685,
      "subStages": [
        {
          "stageId": "1",
          "state": "FINISHED",
          "done": true,
          "nodes": 1,
          "totalSplits": 17,
          "queuedSplits": 0,
          "runningSplits": 0,
          "completedSplits": 17,
          "cpuTimeMillis": 5,
          "wallTimeMillis": 80,
          "processedRows": 29,
          "processedBytes": 1685,
          "subStages": [
            {
              "stageId": "2",
              "state": "FINISHED",
              "done": true,
              "nodes": 1,
              "totalSplits": 1,
              "queuedSplits": 0,
              "runningSplits": 0,
              "completedSplits": 1,
              "cpuTimeMillis": 16,
              "wallTimeMillis": 395,
              "processedRows": 29,
              "processedBytes": 2743,
              "subStages": []
            }
          ]
        }
      ]
    },
    "runtimeStats": {
      "S2-taskQueuedTimeNanos": {
        "name": "S2-taskQueuedTimeNanos",
        "unit": "NANO",
        "sum": 105344250,
        "count": 1,
        "max": 105344250,
        "min": 105344250
      },
      "S0-taskScheduledTimeNanos": {
        "name": "S0-taskScheduledTimeNanos",
        "unit": "NANO",
        "sum": 9791421,
        "count": 1,
        "max": 9791421,
        "min": 9791421
      },
      "getColumnMetadataTimeNanos": {
        "name": "getColumnMetadataTimeNanos",
        "unit": "NANO",
        "sum": 26291,
        "count": 1,
        "max": 26291,
        "min": 26291
      },
      "getLayoutTimeNanos": {
        "name": "getLayoutTimeNanos",
        "unit": "NANO",
        "sum": 528166690,
        "count": 5,
        "max": 116850294,
        "min": 87751379
      },
      "S0-taskBlockedTimeNanos": {
        "name": "S0-taskBlockedTimeNanos",
        "unit": "NANO",
        "sum": 501382737,
        "count": 1,
        "max": 501382737,
        "min": 501382737
      },
      "S0-taskQueuedTimeNanos": {
        "name": "S0-taskQueuedTimeNanos",
        "unit": "NANO",
        "sum": 42479683,
        "count": 1,
        "max": 42479683,
        "min": 42479683
      },
      "S0-taskElapsedTimeNanos": {
        "name": "S0-taskElapsedTimeNanos",
        "unit": "NANO",
        "sum": 43242985419,
        "count": 1,
        "max": 43242985419,
        "min": 43242985419
      },
      "getColumnHandleTimeNanos": {
        "name": "getColumnHandleTimeNanos",
        "unit": "NANO",
        "sum": 64889,
        "count": 1,
        "max": 64889,
        "min": 64889
      },
      "S1-taskScheduledTimeNanos": {
        "name": "S1-taskScheduledTimeNanos",
        "unit": "NANO",
        "sum": 79800908,
        "count": 1,
        "max": 79800908,
        "min": 79800908
      },
      "S1-taskBlockedTimeNanos": {
        "name": "S1-taskBlockedTimeNanos",
        "unit": "NANO",
        "sum": 7471754619,
        "count": 1,
        "max": 7471754619,
        "min": 7471754619
      },
      "optimizerTimeNanos": {
        "name": "optimizerTimeNanos",
        "unit": "NANO",
        "sum": 640370414,
        "count": 1,
        "max": 640370414,
        "min": 640370414
      },
      "S2-taskElapsedTimeNanos": {
        "name": "S2-taskElapsedTimeNanos",
        "unit": "NANO",
        "sum": 518558594,
        "count": 1,
        "max": 518558594,
        "min": 518558594
      },
      "getMaterializedViewTimeNanos": {
        "name": "getMaterializedViewTimeNanos",
        "unit": "NANO",
        "sum": 30797,
        "count": 1,
        "max": 30797,
        "min": 30797
      },
      "S1-driverCountPerTask": {
        "name": "S1-driverCountPerTask",
        "unit": "NONE",
        "sum": 17,
        "count": 1,
        "max": 17,
        "min": 17
      },
      "S2-driverCountPerTask": {
        "name": "S2-driverCountPerTask",
        "unit": "NONE",
        "sum": 1,
        "count": 1,
        "max": 1,
        "min": 1
      },
      "S1-taskElapsedTimeNanos": {
        "name": "S1-taskElapsedTimeNanos",
        "unit": "NANO",
        "sum": 518198076,
        "count": 17,
        "max": 108828984,
        "min": 87751379
      },
      "S1-taskQueuedTimeNanos": {
        "name": "S1-taskQueuedTimeNanos",
        "unit": "NANO",
        "sum": 26468654,
        "count": 17,
        "max": 14544368,
        "min": 264660
      },
      "S1-taskBlockedTimeNanos": {
        "name": "S1-taskBlockedTimeNanos",
        "unit": "NANO",
        "sum": 7454917683,
        "count": 17,
        "max": 723504235,
        "min": 1184050
      },
      "S1-taskScheduledTimeNanos": {
        "name": "S1-taskScheduledTimeNanos",
        "unit": "NANO",
        "sum": 79950554,
        "count": 17,
        "max": 8761998,
        "min": 22391
      },
      "S0-taskElapsedTimeNanos": {
        "name": "S0-taskElapsedTimeNanos",
        "unit": "NANO",
        "sum": 43278621276,
        "count": 1,
        "max": 43278621276,
        "min": 43278621276
      },
      "S2-taskBlockedTimeNanos": {
        "name": "S2-taskBlockedTimeNanos",
        "unit": "NANO",
        "sum": 52262327,
        "count": 1,
        "max": 52262327,
        "min": 52262327
      },
      "S2-taskScheduledTimeNanos": {
        "name": "S2-taskScheduledTimeNanos",
        "unit": "NANO",
        "sum": 39787625,
        "count": 1,
        "max": 39787625,
        "min": 39787625
      },
      "S2-taskQueuedTimeNanos": {
        "name": "S2-taskQueuedTimeNanos",
        "unit": "NANO",
        "sum": 53366618,
        "count": 1,
        "max": 53366618,
        "min": 53366618
      },
      "S2-taskElapsedTimeNanos": {
        "name": "S2-taskElapsedTimeNanos",
        "unit": "NANO",
        "sum": 528371707,
        "count": 1,
        "max": 528371707,
        "min": 528371707
      },
      "S1-driverRowsPerTask": {
        "name": "S1-driverRowsPerTask",
        "unit": "NONE",
        "sum": 29,
        "count": 1,
        "max": 29,
        "min": 29
      }
    }
  }
}

```