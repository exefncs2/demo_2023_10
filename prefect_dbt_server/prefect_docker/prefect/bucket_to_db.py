# -*- coding:utf-8 -*-
from prefect import flow,task
from prefect_gcp import  GcsBucket , GcpCredentials
import os
from psycopg2 import sql
import psycopg2
from datetime import date
import atexit
import json

# 設定通用值
bucket_name = f"<your bucket_name>"
directory_path = "<your bucket_directory_path>"
db_schema = "<your schema>"
json_origin_table = "<origin table>"

BLOCK_NAME =  os.environ["CREDENTIALS_BLOCK_NAME"]
gcp_credentials = GcpCredentials.load(BLOCK_NAME)

# psql連線
connection = psycopg2.connect(
    host='<your_host>',
    user='<your_user>',
    password='<your_pass>',
    database='<your_db>'
)

# 上傳json到psql
@task
def update_json(json_str):
    cursor = connection.cursor()
    
    # 构建插入数据的SQL查询
    insert_query = sql.SQL(f"INSERT INTO {db_schema}.{json_origin_table} (data, insert_date) VALUES (%s, %s);")
    current_date = date.today().isoformat()
    cursor.execute(insert_query, (json_str,current_date))

    connection.commit()  
     
    cursor.close()

@task
def clear_table(table_name):
    cursor = connection.cursor()
    
    # 构建删除数据的SQL查询
    delete_query = sql.SQL("DELETE FROM {}.{}").format(sql.Identifier(db_schema),sql.Identifier(table_name))
    
    # 执行删除查询
    cursor.execute(delete_query)
    connection.commit()
    cursor.close()

@flow(name="get_json_with_GCPbucket",log_prints=True)
def get_json_with_GCPbucket():
    # 定義 bucket
    gcs_bucket = GcsBucket(bucket = bucket_name,
                           gcp_credentials=gcp_credentials)
    
    # 資料夾list
    floder_file_name = gcs_bucket.list_blobs(directory_path)
    
    # 清空db
    print(f'clear {json_origin_table}')
    clear_table(json_origin_table)
    
    # 迴圈處裡list
    for file_name in floder_file_name:
        print(f"read {file_name.name} ...")
        if file_name.name.endswith('.json'):
            # 文件是JSON文件
            print(file_name.name,' is  json.')
            json_string = file_name.download_as_string()
            json_str_decode = json_string.decode('utf-8')
            json_data = json.loads(json_str_decode)
            json_str = json.dumps(json_data)
            
            #寫入DB
            update_json(json_str)
            print(f"{file_name.name} is join {json_origin_table}")
        else:
            # 文件不是JSON文件
            print(file_name.name,' is not json.')
            
    print('get bucket json to db is flash.')



# 注册在应用程序关闭时执行的函数
@task
def close_db_connection():
    connection.close()
    print('--------------------db link stop.---------------------')
    print()
    print('all flish.')

if __name__ == "__main__":
    # create your  deployment
    flow = get_json_with_GCPbucket.serve(name="GCPbucket", interval=600)
    close_db_connection()

# end this work
atexit.register(close_db_connection)
