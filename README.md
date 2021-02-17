# airflow

Master Apache Airflow from A to Z

## Usage
```
docker-compose up -d
```

[Airflow](http://localhost:8080)

[PgAdmin](http://localhost:5050)

## Concurrent tasks processing
Find the [dag](https://github.com/robincvlr/airflow/blob/main/dags/par/dag_par_1.py) related to this computation

![Alt text](./doc/img/concurrent.png?raw=true "Gantt concurrent processing")
*Gantt concurrent processing*

## Sequential tasks processing
Find the [dag](https://github.com/robincvlr/airflow/blob/main/dags/single/dag_single_1.py) related to this computation

![Alt text](./doc/img/single.png?raw=true "Gantt sequential processing")
*Gantt sequential processing*

## Metadata Adhoc queries

Access your DAG metadata from Airflow UI or PgAdmin.

### PgAdmin
![Alt text](./doc/img/pgadmin_query.png?raw=true)

### Airflow UI
![Alt text](./doc/img/airflow_query.png?raw=true)
