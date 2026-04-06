from airflow.sdk import dag, task
from airflow.exceptions import AirflowException
from pendulum import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['test']
)

def test_dag():
    @task
    def cli(val):
        raise AirflowException("This is a test exception")
        print(f"Received value: {val}")
        val = 42
        return val
    
    cli(80)
test_dag()