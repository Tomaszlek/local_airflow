from airflow.sdk import dag, task 
from airflow.providers.standard.operators.bash import BashOperator
from pendulum import datetime
import random

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['partial_expand']
)
def my_dag():
    @task
    def get_files():
        return [f"file_{nb}" for nb in range(1, random.randint(3, 5))]
    
    @task
    def download_files(folder: str, file: str):
        return f" ls {folder}/{file}; exit 0"

    files = download_files.partial(folder="/usr/local").expand(file=get_files())

    BashOperator.partial(task_id="ls file").expand(bash_command=files)