from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'freanu',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_catchup_backfill_v02',
    default_args=default_args,
    start_date=datetime(2024,6,10),
    schedule_interval='@daily',
    catchup=False,
    

) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )

    task1
