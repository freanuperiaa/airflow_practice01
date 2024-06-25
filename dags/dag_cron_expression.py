from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'freanu',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}


with DAG(
    dag_id='dag_with_cron_expression_v05',
    default_args=default_args,
    start_date=datetime(2024,6,1),
    schedule_interval='0 0 * * Mon',
    catchup=True

) as dag:
    
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a Bash Operator command!'
    )

    task1
