from airflow.decorators import dag, task
from pendulum import datetime
import requests

from airflow.sensors.base import PokeReturnValue

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['sensor']
)
def sensor_decorator():
    @task.sensor(poke_interval=30, timeout=3600, mode='poke')
    def check_shibe_availability() -> PokeReturnValue:
        response = requests.get("https://shibe.online/api/shibes?count=1")
        
        print(response.status_code)
        if response.status_code == 200:
            condition_met = True
            operator_return_value = response.json()
        else:
            condition_met = False
            operator_return_value = None
            print(f"Shibe API is not available. Status code: {response.status_code}")
    
        return PokeReturnValue(is_done=condition_met, xcom_value=operator_return_value)