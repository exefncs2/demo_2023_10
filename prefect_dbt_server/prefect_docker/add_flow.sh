#!/bin/bash
cd /work
directory="logs"

if [ ! -d "$directory" ]; then
    mkdir -p "$directory"
    echo "目录已创建：$directory"
else
    echo "目录已存在：$directory"
fi

nohup python /work/prefect/main.py  > ./logs/main.log 2>&1 &

