# -*- coding:utf-8 -*-
# Main.py
from prefect import Flow,serve


# 註冊 Flow1 和 Flow2
from bucket_to_db import get_json_with_GCPbucket
from dbt_cil import trigger_dbt_flow



# 設定依賴關係
flow1 = trigger_dbt_flow.to_deployment(name="trigger_dbt_flow", interval=600)
flow2 = get_json_with_GCPbucket.to_deployment(name="get_json_with_GCPbucket", interval=600)
serve(flow1,flow2)
