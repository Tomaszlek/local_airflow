from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from pendulum import datetime

@dag(
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['sensor']
)

def second_dag():
    @task
    def run_me():
        print("Running task...")
    
    run_me()

second_dag()