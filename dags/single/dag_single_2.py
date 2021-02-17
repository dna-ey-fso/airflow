from airflow import DAG
from airflow.operators.subdag_operator import SubDagOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from single.dag_single_sub_2 import subdag


DAG_NAME = "single_dag_example_2"


args = {
    'owner': 'airflow',
}


dag = DAG(
    dag_id=DAG_NAME, default_args=args, start_date=days_ago(1), schedule_interval='@once'
)


start = DummyOperator(
    task_id='start',
    dag=dag,
)


subdag_1 = SubDagOperator(
    task_id='section-1',
    subdag=subdag(DAG_NAME, 'section-1', dag.start_date, dag.schedule_interval, args),
    dag=dag,
)


end = DummyOperator(
    task_id='end',
    dag=dag,
)


start >> subdag_1 >> end
