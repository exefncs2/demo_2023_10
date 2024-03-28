# elementary 說明

### 安裝
```
pip install elementary-data
```

### 修改[packages.yml](packages.yml)後執行
```
dbt deps
```

### 修改[dbt_project.yml](dbt_project.yml)


### 建立預設表
```
dbt run --select elementary
```

### 增加user
```
dbt run-operation create_elementary_user
```

### 執行後會得到資訊 增加資訊[profiles.yml](profiles.yml)

### 執行後會得到資訊 要到sql執行
```
CREATE USER elementary WITH PASSWORD 'AVDOpKrB8BiEmEIt8bTsYLrEjizHkJOW';
GRANT USAGE ON SCHEMA dbt TO elementary;
ALTER DEFAULT PRIVILEGES IN SCHEMA dbt GRANT SELECT ON TABLES TO elementary;
```

### 給予權限
```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA dbt TO elementary;
```

### 執行
```
edr report
```