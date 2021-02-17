# airflow

Master Apache Airflow from A to Z

## Usage
```
docker-compose up -d
```

UI available at http://localhost:8080.

## Concurrent tasks processing
Find the [dag](https://github.com/robincvlr/airflow/blob/main/dags/par/dag_par_1.py) related to this computation

![Alt text](./doc/img/concurrent.png?raw=true "Gantt concurrent processing")
*Gantt concurrent processing*

## Sequential tasks processing
Find the [dag](https://github.com/robincvlr/airflow/blob/main/dags/single/dag_single_1.py) related to this computation

![Alt text](./doc/img/single.png?raw=true "Gantt sequential processing")
*Gantt sequential processing*