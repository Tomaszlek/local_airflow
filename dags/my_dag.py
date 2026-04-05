from airflow.sdk import dag, task, chain
from airflow.providers.standard.operators.python import PythonOperator
from pendulum import datetime

def _task_a():
    print("Hello, Airflow!")

@dag(
        schedule="@daily", 
        start_date=datetime(2024, 1, 1),
        description="A simple DAG that prints a message",
        tags=["example"],
        max_consecutive_failed_dag_runs=3
)
def my_dag():
    @task
    def task_a():
        print("Hello from Task A!")

    @task
    def task_b():
        print("Hello from Task B!")

    @task 
    def task_c():
        print("Hello from Task C!")

    chain(task_a, [task_b, task_c])

my_dag()