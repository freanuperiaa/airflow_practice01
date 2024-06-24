from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'freanu',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(ti):
    print('Running using Python Operator...')

    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    
    print(f'Hello World!!! I am {first_name} {last_name} and I am {age} years old')
    print('------------------------------')

# def get_name():
#     return 'Games Reid'

def get_name(ti):
    ti.xcom_push(key='first_name', value='Games')
    ti.xcom_push(key='last_name', value='Reid')
    # ti.xcom_push(key='age', value='24')

def get_age(ti):
    ti.xcom_push(key='age', value='24')

with DAG(
    default_args=default_args,
    dag_id='dag_py_operator_v06',
    description='Our first dag using Python Operator',
    start_date=datetime(2024, 6, 24),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={
            # 'name': 'Games Reid',
            # 'age': '24'
        }
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
    # execute task2 first, then, 
    # thru xcoms_pull() inside task1, retrieve return value from task2

