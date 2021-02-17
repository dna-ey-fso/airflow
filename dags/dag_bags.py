import os 
from airflow.models import DagBag


#################################
# DAG BAG Configuration path
#################################
dags_dirs = [
    "~/parallel",
    "~/sequential",
    "~/templates",
    "~/triggers",
    "~/sensors"
]


#################################
# Iteration loop
#################################
for dir in dags_dirs:
    dag_bag = DagBag(os.path.expanduser(dir))
    if dag_bag:
        for dag_id, dag in dag_bag.dags.items():
            globals()[dag_id] = dag
    else:
        print(f"dag bag not valid: {dir}")

