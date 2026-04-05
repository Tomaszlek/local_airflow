from airflow.decorators import dag, task, chain
from airflow.sensors.filesystem import FileSensor
from pendulum import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['sensor']
)

def first_dag():
    wait_for_files = FileSensor(
        task_id = 'wait_for_files',
        fs_conn_id = 'fs_default'
    ).expand(
        filepath = ['data1.csv', 'data2.csv', 'data3.csv']
    )

    @task
    def process_file():
        print("Processing file...")

    chain(wait_for_files, process_file())

first_dag()