from datetime import datetime, timedelta
from airflow import DAG, macros
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


TEMPLATED_TS = """{{ ds_nodash }}"""
FILENAME = "extract.csv"
FILEPATH = "/tmp/"


default_args = {
    'owner': 'Airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'catchup': True,
    'schedule_interval': '@daily'
}


with DAG(dag_id='template_dag', default_args=default_args) as dag:


    create_file = BashOperator(
        task_id='task_create_file',
        bash_command=f"""
            touch {FILEPATH}{FILENAME}
        """
    )


    move_file = BashOperator(
        task_id='task_move_file',
        bash_command=f"""
            mv {FILEPATH}{FILENAME} {FILEPATH}{TEMPLATED_TS}_{FILENAME}
        """
    )


    check_file = BashOperator(
        task_id='task_check_file',
        bash_command=f"""
            test -f {FILEPATH}{TEMPLATED_TS}_{FILENAME}
        """
    )


    create_file >> move_file >> check_file