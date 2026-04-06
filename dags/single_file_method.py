from airflow.sdk import dag, task
from pendulum import datetime

def create_dag(filename):
    @dag(
        dag_id=f'{filename}_dag',
        schedule="@daily",
        start_date=datetime(2024, 1, 1),
        catchup=False,
        tags=['single_file']
    )

    @task
    def extract(filename):
        return filename
    
    @task
    def process(filename):
        return filename
    
    @task
    def send_email(filename):
        print(filename)
        return filename
    
    send_email(process(extract(filename)))

for file in ["file1.csv", "file2.csv", "file3.csv"]:
    globals()[f"{file}_dag"] = create_dag(file)