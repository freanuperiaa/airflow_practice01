# Coder2j Airflow Tutorial

just following the tutorial from coder2j.
https://www.youtube.com/watch?v=K9AnJ9_ZAXE



```
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
    
```


So far it seems pretty straightforward.

We instantiate Airflow's DAG Class first, then we define tasks with operators (task1, task2)

then, we can set dependencies or just simply call those tasks