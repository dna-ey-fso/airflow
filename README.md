# airflow

Master Apache Airflow from A to Z

## Usage
```
docker-compose up -d
```

[Airflow](http://localhost:8080)

[PgAdmin](http://localhost:5050)

## Concurrent tasks processing
Find the [dag](https://github.com/robincvlr/airflow/blob/main/dags/parallel/dag_par_1.py) related to this computation

![Alt text](./doc/img/concurrent.png?raw=true "Gantt concurrent processing")
*Gantt concurrent processing*

## Sequential tasks processing
Find the [dag](https://github.com/robincvlr/airflow/blob/main/dags/sequential/dag_single_1.py) related to this computation

![Alt text](./doc/img/single.png?raw=true "Gantt sequential processing")
*Gantt sequential processing*

## Metadata Adhoc queries

Access your DAG metadata from Airflow UI or PgAdmin.

### PgAdmin
![Alt text](./doc/img/pgadmin_query.png?raw=true)

### Airflow UI
![Alt text](./doc/img/airflow_query.png?raw=true)

## Concepts
- [Pool](https://github.com/robincvlr/airflow/blob/main/dags/parallel/dag_pool_1.py): limit the execution parallelism on arbitrary sets of tasks

- [XCOM](https://github.com/robincvlr/airflow/blob/main/dags/parallel/dag_pool_1.py): exchange messages between tasks

- [SubDAG](https://github.com/robincvlr/airflow/blob/main/dags/sequential/dag_single_sub_2.py): Create a subDAGs, a smaller unit of process

- [DAGBags](https://github.com/robincvlr/airflow/blob/main/dags/dag_bags.py): Manage your dags with modules

- [Triggers](https://github.com/robincvlr/airflow/blob/main/dags/triggers/): Trigger a DAG from another

- [Templates](https://github.com/robincvlr/airflow/blob/main/dags/templates): How to use Airflow templating

- [Logging](https://github.com/robincvlr/airflow/blob/main/conf/log_config.py): How to configure logging and monitor Airflow

## Not covered
- Security
- Scalability with Celery
- Queueing using KEDA
