import os
from datetime import date, timedelta
from airflow import DAG
from airflow import DAG
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtSnapshotOperator,
    DbtRunOperator,
    DbtTestOperator
)
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

dbt_dir = os.environ.get("update_dbt_dir")

default_args = {
  'owner': 'admin',
  'dir': dbt_dir,
  'start_date': days_ago(0)
}

with DAG(dag_id='dbt_update', default_args=default_args, schedule_interval='@daily') as dag:

#   dbt_seed = DbtSeedOperator(
#     task_id='dbt_seed',
#   )

#   dbt_snapshot = DbtSnapshotOperator(
#     task_id='dbt_snapshot',
#   )
  def my_python_function(**context):
    omop_table_name = Variable.get("omop_table_name", default_var="default_value")
    dbt_run = DbtRunOperator(
        task_id='dbt_run',
        select=f'tag:{omop_table_name}',
        dag=dag
    )
    dbt_run.execute(context)

  get_parameter_task = PythonOperator(
        task_id='get_parameter',
        python_callable=my_python_function,
        provide_context=True
    )

  dbt_test = DbtTestOperator(
    task_id='dbt_test',
    retries=0,  # Failing tests would fail the task, and we don't want Airflow to try again
  )

  #dbt_seed >> dbt_snapshot >>
  get_parameter_task >> dbt_test