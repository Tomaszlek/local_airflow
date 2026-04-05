from airflow.sdk import dag, task, chain
from pendulum import datetime 

@dag(
        schedule="@daily",
        start_date=datetime(2025, 1, 1),
        description="A DAG to check the data",
        tags=["data_engineering"]
)
def check_dag():
    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy'
    
    @task.bash
    def check_file():
        return 'test -f /tmp/dummy'
    
    @task 
    def read_file():
        print(open('/tmp/dummy', 'rb').read())

    chain(create_file(), check_file(), read_file())
    
check_dag()
