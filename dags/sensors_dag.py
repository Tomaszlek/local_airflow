from airflow.sdk import dag, task
from airflow.sensors.python import PythonSensor
from pendulum import datetime

def _condition():
    return False

@dag(
        schedule="@daily", 
        start_date=datetime(2025, 1, 1),
        description="A DAG that demonstrates the use of sensors",
        tags=["sensors"]
)
def sensors_dag():
    waiting_for_condition = PythonSensor(
        task_id="waiting_for_condition",
        python_callable=_condition,
        poke_interval=10,  # Check every 10 seconds
        timeout=60,       # Timeout after 60 seconds
    )
