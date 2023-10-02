from dagster import job
from dagster_dbt import dbt_run_op, dbt_cli_resource
# from dagster import schedule,ScheduleEvaluationContext,RunRequest
@job(resource_defs={"dbt":dbt_cli_resource})
def dbt_cli_job():
    dbt_run_op()

# @schedule(job=dbt_cli_job, cron_schedule="0 0 * * *")
# def configurable_job_schedule2(context: ScheduleEvaluationContext):
#     scheduled_date = context.scheduled_execution_time.strftime("%Y-%m-%d")
#     return RunRequest(
#         run_key=None,
#         run_config={
#             "ops": {"configurable_op": {"config": {"scheduled_date": scheduled_date}}}
#         },
#         tags={"date": scheduled_date},
#     )
