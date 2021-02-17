from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


parameters = {
    "dag_id": "single_dag_example_1",
    "start_year": 2021,
    "start_month": 2,
    "start_day": 16,
    "schedule_interval": "0 15 * * *",
    "timeout": 5
}


with DAG(
    dag_id=parameters["dag_id"],
    start_date=datetime(parameters["start_year"], parameters["start_month"], parameters["start_day"]),
    schedule_interval=parameters["schedule_interval"],
    catchup=True
) as dag:


    def dummy_task_1():
        print("Task 1 should be executed in parrallel with Task 2")


    def dummy_task_2():
        print("Task 2 should be executed in parrallel with Task 1")
    

    def dummy_task_3():
        print("Task 3 should wait for Task 1 & 2")


    task_1 = PythonOperator(
        task_id='task_1',
        python_callable=dummy_task_1,
        dag=dag,
        execution_timeout=timedelta(seconds=parameters["timeout"])
    )


    task_2 = PythonOperator(
        task_id='task_2',
        python_callable=dummy_task_2,
        dag=dag,
        execution_timeout=timedelta(seconds=parameters["timeout"])
    )


    task_3 = PythonOperator(
        task_id='task_3',
        python_callable=dummy_task_3,
        dag=dag,
        execution_timeout=timedelta(seconds=parameters["timeout"])
    )


    task_1 >> task_2 >> task_3