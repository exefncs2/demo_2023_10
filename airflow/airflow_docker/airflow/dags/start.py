#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator
import json

def get_http_response_code(**kwargs):
    ti = kwargs['ti']
    http_response = ti.xcom_pull(task_ids='call_api_task')
    if http_response:
        http_response_dict = json.loads(http_response)
        http_status_code = http_response_dict.get('statusCode')
        print("HTTP Status Code:", http_status_code)
        return http_status_code

# 定義 DAG 的預設參數
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 初始化一個 DAG 物件
dag = DAG(
    'api_pass_dag',
    default_args=default_args,
    description='測試用API',
    schedule_interval=timedelta(days=1),  # 按天間隔運行
)

# 定義 API 的 URL
api_point = 'work01'

# 創建一個 HttpSensor 任務，用於檢查 API 是否可用

api_task = SimpleHttpOperator(
    task_id='call_api_task',
    method='POST',
    http_conn_id='http_default',
    endpoint=api_point,  # Replace with the appropriate container name and endpoint
    data={},  # You can pass data if needed
    dag=dag,
)

# 創建一個 PythonOperator 任務，用於解析 HTTP 回傳的狀態碼
parse_response_task = PythonOperator(
    task_id='parse_response_task',
    python_callable=get_http_response_code,
    provide_context=True,
    dag=dag,
)

# 設定任務之間的依賴關係
api_task >> parse_response_task

