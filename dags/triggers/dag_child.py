from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'Airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'catchup': True,
    'schedule_interval': '@daily'
}


with DAG(dag_id='dag_child', default_args=default_args) as dag:


    task_1 = BashOperator(
        task_id="bash_task",
        bash_command="echo 'Child deployed'"
    )