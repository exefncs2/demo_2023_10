cd /work/demo
dbt clean
dbt deps

cd /work/prefect
prefect server start --host 0.0.0.0 

