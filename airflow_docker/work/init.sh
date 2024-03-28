#!/bin/bash
echo "-------------------------init--------------------------------"
# 定义工作目录和初始化文件路径
WORK_DIR=/opt/airflow/work
INIT_FILE=$WORK_DIR/.init

echo ! -f "$INIT_FILE"
if [ ! -f "$INIT_FILE" ]; then
    echo "-----------------Initialization steps start---------------" 
    cd /opt/airflow/work/imgenie-dbt
    
    pip3 install --upgrade pip 
    pip3 install -r requirements.txt 
    
    pip3 install airflow-dbt==0.4.0 # 次序必須最後面不然會有問題

    dbt clean
    dbt deps
    
    cd /opt/airflow/work/imgenie-dbt-bigquery
    
    dbt clean
    dbt deps

    echo "========================================initialize airflow========================================"
    cd /opt/airflow/


    # Initialize Airflow database
    airflow db init    

    echo "==================================== end init ======================================="
# 在操作完成后创建 .init 文件
     # 获取当前日期和时间
    current_datetime=$(date)
    
    # 获取启动容器的用户名
    container_user=$(whoami)
    
    # 记录启动时间、日期、记录者和用户到文件
    echo "Container started by $container_user on $current_datetime"
    
    echo "Container started by $container_user on $current_datetime" >> $INIT_FILE
else
    echo ".init file exists, skipping initialization steps"
fi

echo "-------------------start start.sh------------------------"
sh /opt/airflow/work/start.sh
