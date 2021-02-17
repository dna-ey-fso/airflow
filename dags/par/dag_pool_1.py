from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime
 

default_args = {
    'owner': 'Airflow',
    'start_date': days_ago(1)
}
 

with DAG(
    dag_id='pool_dag_example_1', 
    schedule_interval='@once', 
    default_args=default_args, 
    catchup=True
) as dag:
   

    get_forex_rate_EUR = SimpleHttpOperator(
        task_id='get_forex_rate_EUR',
        method='GET',
        priority_weight=1,
        pool='batch_pool',
        http_conn_id='forex_api',
        endpoint='/latest?base=EUR',
        queue='default',
        xcom_push=True,
        dag=dag
    )


    get_forex_rate_USD = SimpleHttpOperator(
        task_id='get_forex_rate_USD',
        method='GET',
        priority_weight=2,
        pool='batch_pool',
        http_conn_id='forex_api',
        endpoint='/latest?base=USD',
        queue='default',
        xcom_push=True,
        dag=dag
    )


    # Will use XCOM json data in the next Operator
    bash_command="""
        {% for task in dag.task_ids %}
            echo "{{ task }}"
            echo "{{ ti.xcom_pull(task) }}"
        {% endfor %}
    """
 

    show_data = BashOperator(
        task_id='show_result',
        bash_command=bash_command,
        queue='default',
        dag=dag
    )
 

    [get_forex_rate_EUR, get_forex_rate_USD] >> show_data