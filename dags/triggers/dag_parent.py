from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'Airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'catchup': True,
    'schedule_interval': '@daily'
}


with DAG(dag_id='dag_parent', default_args=default_args) as dag:


    task_1 = DummyOperator(
        task_id='does_nothing',
        dag=dag
    )


    task_2 = TriggerDagRunOperator(
        task_id="trigger_something",
        trigger_dag_id="dag_child"
    )


    task_1 >> task_2