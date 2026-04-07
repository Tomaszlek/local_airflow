from airflow.sdk import dag, task
from pendulum import datetime

@dag(
    dag_id='sharing_dag',
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['sharing']
)

def sharing_dag():
    @task
    def task_1():
        return 42
    
    @task(do_xcom_push=False)
    def task_2(value: int) -> dict[str, int]:
        print(value)
        return {"first_value": value, "second_value": value * 2}
    
    @task
    def task_3(first_value: int, second_value: int):
        print(f"First value: {first_value}, Second value: {second_value}")

    values = task_2(task_1())
    task_3(values["first_value"], values["second_value"])

sharing_dag()
