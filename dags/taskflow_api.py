from airflow.decorators import dag, task
from airflow.providers.standard.operators.python import get_current_context
from pendulum import datetime

@dag(
    dag_id='taskflow_api_dag',
    schedule="@once",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['taskflow_api']
)
def taskflow_api():
    @task(retries=3)
    def start():
        context = get_current_context()
        print(context)
        return 'success'
    
    @task.branch
    def choose_task(next_task: str):
        return next_task
    
    @task(retries=1)
    def success():
        print('success')

    @task(retries=1)
    def failure():
        print('failure')
    
    next_task = choose_task(start())
    success() if next_task == 'success' else failure()
taskflow_api()    

