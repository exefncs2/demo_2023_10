import os
from datetime import time, timedelta, datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryGetDatasetTablesOperator,
    BigQueryGetDataOperator
)
from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import json
import uuid

# 設定通用值
bucket_name = os.environ.get("bucket_name")
db_schema = os.environ.get("schema")
json_origin_table = os.environ.get("update_origin_table_name")
directory_path = os.environ.get("update_bucket_path")
postgres_conn = os.environ.get("postgres_conn")
google_cloud_storage_conn = os.environ.get("google_cloud_storage_conn")
dataset = os.environ.get("dataset_update")

# 定義 DAG 的默認參數
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}



# 在 DAG 內定義任務
with DAG(
    'bigquery_to_postgres_dag_update',
    default_args=default_args,
    description='從 GCS 轉移 JSON 檔案到 PostgreSQL update',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1)
) as dag:
    # BigQuery 任務：獲取資料集中的所有表格
    get_dataset_tables = BigQueryGetDatasetTablesOperator(
        task_id="get_dataset_tables",
        dataset_id=dataset,
        gcp_conn_id=google_cloud_storage_conn,
    )
    
    def get_data_task(table_id, dataset_id, **kwargs):
        get_data = BigQueryGetDataOperator(
        task_id=f"get_data_{table_id}",
        dataset_id=dataset_id,
        table_id=table_id,
        
        gcp_conn_id=google_cloud_storage_conn,
        dag=dag,
    )
        downloaded_data = get_data.execute(context=kwargs)
        return downloaded_data[0][0]
    
    # Python 任務：將資料從 BigQuery 拉取到 PostgreSQL
    def output_db_exec(**kwargs):
        insert_json_tasks = []
        now = datetime.now()
        current_timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        task_instance = kwargs['ti']
        
        # 使用 get_dataset_tables 任務的 task_id 來拉取結果
        get_dataset_tables_task_id = 'get_dataset_tables'
        table_list = task_instance.xcom_pull(task_ids=get_dataset_tables_task_id, key='return_value')
        
        # 迴圈處理每個表格的資料
        for index, table in enumerate(table_list):
            print(table['tableId'],"<<<<<<<<<<<<<")
            
            # 使用 get_data_{index} 任務的 task_id 來拉取結果
            downloaded_data = get_data_task(table['tableId'], dataset, **kwargs)
            print( downloaded_data )
            
            random_uuid = uuid.uuid4()
            type = "update" # 根據unique_key更新
            query = f"INSERT INTO {db_schema}.{json_origin_table} (insert_id ,data , create_time,type) VALUES ('{random_uuid}','{downloaded_data}', '{current_timestamp}','{type}');"

            
            # PostgreSQL 任務：插入資料到 PostgreSQL
            insert_task = PostgresOperator(
                task_id=f'insert_json_{index}',
                sql=query,
                postgres_conn_id=postgres_conn,
                autocommit=True,
                dag=dag,
            )
            insert_json_tasks.append(insert_task)
        
        # 執行所有 PostgreSQL 插入任務
        for task in insert_json_tasks:
            task.execute(context=kwargs)
    
    # PythonOperator 任務
    output_db = PythonOperator(
        task_id='output_db',
        python_callable=output_db_exec,
        provide_context=True,
    )

    # 定義 DAG 的任務之間的依賴性
    get_dataset_tables >> output_db
