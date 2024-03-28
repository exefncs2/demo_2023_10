import os
from datetime import time, timedelta,datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

# 設定通用值
bucket_name = os.environ.get("bucket_name")
db_schema = os.environ.get("schema")
json_origin_table = os.environ.get("origin_table_name")
directory_path = os.environ.get("bucket_path")
dbt_dir = os.environ.get("dbt_dir")
postgres_conn = os.environ.get("postgres_conn")
google_cloud_storage_conn = os.environ.get("google_cloud_storage_conn")

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'dir': dbt_dir,
}

with DAG(
    'once_do_all',
    default_args=default_args,
    description='Transfer JSON files from GCS to PostgreSQL & exec dbt',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1)
) as dag:
    trigger_getdata_dag = TriggerDagRunOperator(
    task_id='trigger_getdata_dag',
    trigger_dag_id='bigquery_to_postgres_dag',
    conf={"schedule_interval": "0 0 * * *"},  # 新的调度间隔
    dag=dag,
)
    
    trigger_dbt_dag = TriggerDagRunOperator(
    task_id='trigger_dbt_dag',
    trigger_dag_id='dbt',
    conf={"schedule_interval": "0 0 * * *"},  # 新的调度间隔
    dag=dag,
)
    trigger_getdata_dag >> trigger_dbt_dag