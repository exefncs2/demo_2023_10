from dagster import Definitions, load_assets_from_modules
from . import assets # 多個loading assets
from .mydag import dbt_cli_job  #單一job
from .schedules import configurable_job_schedule,configurable_job
from .api_link import api_call_pipeline ,dbt_api_Schedule,api_sensor

all_assets = load_assets_from_modules([assets])


defs = Definitions(  # 這個參數會自動載入 dev的內容
    assets=all_assets,
    jobs=[dbt_cli_job,configurable_job,api_call_pipeline],
    schedules=[configurable_job_schedule,dbt_api_Schedule],
     sensors=[api_sensor],
#     resources=dbt_resource
)
