# -*- coding:utf-8 -*-
from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation

#from bucket_to_db import get_json_with_GCPbucket

@flow(name="trigger_dbt_flow", log_prints=True)
def trigger_dbt_flow() -> str:
    project_dir_name="/work/imgenie-dbt" # defult same
    results = []
    result = DbtCoreOperation(
        commands=[f"dbt run"],
        project_dir=project_dir_name,
        profiles_dir=project_dir_name
    ).run()
    results.append(result)
    print(f"flash 'dbt run'")
    
    result2 = DbtCoreOperation(
        commands=[f"dbt test"],
        project_dir=project_dir_name,
        profiles_dir=project_dir_name
    ).run()
    results.append(result2)
    print(f"flash 'dbt test'")
    
    print('dbt is execute over.')
    return results

if __name__ == "__main__":
    flow = trigger_dbt_flow.serve(name="trigger_dbt_flow", interval=600)
    
    
