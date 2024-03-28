import os
from datetime import time, timedelta,datetime
from airflow import DAG
from airflow.contrib.operators.gcs_list_operator import GoogleCloudStorageListOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.google.cloud.hooks.gcs import parse_json_from_gcs
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import json
import uuid

# 設定通用值
bucket_name = os.environ.get("bucket_name")
db_schema = os.environ.get("schema")
json_origin_table = os.environ.get("origin_table_name")
directory_path = os.environ.get("bucket_path")
postgres_conn = os.environ.get("postgres_conn")
google_cloud_storage_conn = os.environ.get("google_cloud_storage_conn")

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


with DAG(
    'gcs_to_postgres_dag',
    default_args=default_args,
    description='Transfer JSON files from GCS to PostgreSQL',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1)
) as dag:
    # 定義 TaskGroup
    insert_json_tasks=[]
    
    # 上傳json到psql
    def update_json(**kwargs):
        task_instance = kwargs['ti']
        # 使用上一個任務的XCom資料
        file_list = task_instance.xcom_pull(task_ids='list_json_files')
        json_files = [file for file in file_list if file.endswith(".json")]
        
        
        # 刪除資料
        # query=f"DELETE FROM {db_schema}.{json_origin_table}"
        # delete_task = PostgresOperator(
        #         task_id=f'delete_json',
        #         sql=query,
        #         postgres_conn_id="postgres_conn_id",
        #         autocommit=True,
        #         dag=dag,
        #     )
        # insert_json_tasks.append(delete_task)
        
        # 寫入資料
        
        now = datetime.now()
        current_timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        
        for index, json_file in enumerate(json_files):   
            random_uuid = uuid.uuid4()  
            downloaded_data = parse_json_from_gcs(gcp_conn_id=google_cloud_storage_conn, file_uri=f"gs://{bucket_name}/{json_file}")
            downloaded_data = json.dumps(downloaded_data).replace("'", "''")
            query = f"INSERT INTO {db_schema}.{json_origin_table} (insert_id ,data , create_time) VALUES ('{random_uuid}','{downloaded_data}', '{current_timestamp}');"

            insert_task = PostgresOperator(
                task_id=f'insert_json_{index}',
                sql=query,
                postgres_conn_id=postgres_conn,
                autocommit=True,
                dag=dag,
            )
            insert_json_tasks.append(insert_task)
        for task in insert_json_tasks:
            task.execute('')
                
                 
    # 列出所有JSON文件
    list_json_files_task = GoogleCloudStorageListOperator(
        task_id='list_json_files',
        bucket=bucket_name,
        prefix=f"{directory_path}/",
        delimiter='/',
        gcp_conn_id=google_cloud_storage_conn,
    )

    # 更新JSON到PostgreSQL
    update_json_task = PythonOperator(
        task_id='update_json',
        python_callable=update_json,
        provide_context=True,
    )

# 設定工作流程依賴關係
list_json_files_task  >> update_json_task 