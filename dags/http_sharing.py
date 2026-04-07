from airflow.sdk import dag, task
from airflow.providers.http.operators.http import HttpOperator
from pendulum import datetime
import json


@dag(
    "http_sharing_dag",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["sharing"]
)
def http_sharing_dag():
    get_api_task = HttpOperator(
        task_id="get_api_data",
        method="GET",
        endpoint="/entries",
        do_xcom_push=True,
        http_conn_id="api"
    )

    @task
    def parse_results(api_results):
        print(json.loads(api_results))
    
    parse_results(api_results=get_api_task.output)

http_sharing_dag()