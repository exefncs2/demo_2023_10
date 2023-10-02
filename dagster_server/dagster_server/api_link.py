from dagster import schedule, ScheduleEvaluationContext, RunRequest, job, op, Any, In, sensor,Out
import http.client

# 定義呼叫 API 的操作
@op(
    #ins={"api_host": In(str), "api_port": In(str), "api_path": In(str)},
    out={"api_output": Out(Any)}  # 定義輸出
)
def call_api(api_host: str, api_port: str, api_path: str) -> Any:
    api_host = "<your_ip>"# api docker 地址
    api_port = "<your_port>"
    api_path = "<頁面名稱ex:run、flow...>"
    
    conn = http.client.HTTPConnection(api_host, api_port)
    conn.request("POST", f"/{api_path}")
    response = conn.getresponse()
    if response.status == 200:
        data = response.read().decode("utf-8")
        return {"api_output": data}  # 返回輸出
    else:
        raise Exception(f"API 調用失敗，狀態碼：{response.status}")

@op(
    #ins={"api_host": In(str), "api_port": In(str), "api_path": In(str)},
    out={"api_output": Out(Any)}  # 定義輸出
)
def call_api2(api_host: str, api_port: str, api_path: str) -> Any:
    api_host = "<your_ip>"# api docker 地址
    api_port = "<your_port>"
    api_path = "bucket_to_db"
    
    conn = http.client.HTTPConnection(api_host, api_port)
    conn.request("POST", f"/{api_path}")
    response = conn.getresponse()
    if response.status == 200:
        data = response.read().decode("utf-8")
        return {"api_output": data}  # 返回輸出
    else:
        raise Exception(f"API 調用失敗，狀態碼：{response.status}")

@op(
    #ins={"api_host": In(str), "api_port": In(str), "api_path": In(str)},
    out={"api_output": Out(Any)}  # 定義輸出
)
def call_api3(api_host: str, api_port: str, api_path: str) -> Any:
    api_host = "<your_ip>"# api docker 地址
    api_port = "<your_port>"
    api_path = "dbt_exec"
    
    conn = http.client.HTTPConnection(api_host, api_port)
    conn.request("POST", f"/{api_path}")
    response = conn.getresponse()
    if response.status == 200:
        data = response.read().decode("utf-8")
        return {"api_output": data}  # 返回輸出
    else:
        raise Exception(f"API 調用失敗，狀態碼：{response.status}")




# 定義作業
@job
def api_call_pipeline(api_host=str, api_port=str, api_path=str):
    call_api_op = call_api(api_host=api_host, api_port=api_port, api_path=api_path)
    call_api_op2 = call_api2(api_host=api_host, api_port=api_port, api_path=api_path)
    call_api_op3 = call_api3(api_host=api_host, api_port=api_port, api_path=api_path)


# 定義感測器
@sensor(job=api_call_pipeline)
def api_sensor(context):
    # 根據你的需求判斷是否觸發
    should_trigger = True  
    if should_trigger:
        # 如果條件滿足，返回一個 RunRequest 來觸發作業運行
        yield RunRequest(run_key=None, run_config=None, tags=None)
    else:
        # 如果條件不滿足，返回 None
        yield None


# 定義排程
@schedule(job=api_call_pipeline, cron_schedule="* * * * *")
def dbt_api_Schedule(context: ScheduleEvaluationContext):
    scheduled_date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return [RunRequest(tags={"date": scheduled_date})]