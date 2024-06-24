from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'freanu',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is my very first dag. I hope that everything will be fine in the future :")',
    start_date=datetime(2024, 6, 23),
    schedule_interval='@daily'

) as dag:
    
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command='echo hello world! This is the first task!'
    )

    
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo second task running...."
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo third task running.... i will be running after task1 and simultaneously with task 2"
    )
    

    # connecting DAGs: set_downstream/upstream
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    # task2.set_upstream(task1)

    # using the ">>" operator
    task1 >> task2
    task1 >> task3

    # using the ">>" operator to a list of tasks
    task1 >> [task2, task3]
    
