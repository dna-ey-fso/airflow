from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators import BashOperator


def subdag(parent_dag_name, child_dag_name, start_date, schedule_interval, args):
    """
    Generate a DAG to be used as a subdag.

    :param str parent_dag_name: Id of the parent DAG
    :param str child_dag_name: Id of the child DAG
    :param dict args: Default arguments to provide to the subdag
    :return: DAG to use as a subdag
    :rtype: airflow.models.DAG
    """


    dag_subdag = DAG(
        dag_id=f'{parent_dag_name}.{child_dag_name}',
        default_args=args,
        start_date=start_date,
        schedule_interval=schedule_interval
    )


    BashOperator(
        task_id="sub_bash_task_1",
        bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
        dag=dag_subdag
    )


    BashOperator(
        task_id="sub_bash_task_2",
        bash_command='ls -lrta',
        dag=dag_subdag
    )


    return dag_subdag
