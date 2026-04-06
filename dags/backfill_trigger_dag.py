from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from pendulum import datetime

with DAG(
    dag_id='backfill_trigger_dag',
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['backfill']
) as dag:
    
    trigger_backfill = BashOperator(
        task_id='trigger_backfill',
        bash_command='airflow dags backfill '
        '--reset-dagruns -y -s {{dag_run.conf["start_date"]}} -e {{dag_run.conf["end_date"]}} {{dag_run.conf["dag_id"]}}'
    )

    trigger_backfill