from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "data_engineer",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="olist_customer_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    transform = BashOperator(
        task_id="transform_customer",
        bash_command="spark-submit spark/jobs/customer_transform.py"
    )

    load = BashOperator(
        task_id="load_customer",
        bash_command="python etl/load/load_customer_postgres.py"
    )

    transform >> load
