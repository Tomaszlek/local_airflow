from airflow.sdk import dag, task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from pendulum import datetime

@dag(
    schedule=None,
    start_date=datetime(2025, 1, 1),
    tags=["aws"]
)
def aws_s3_dag():
    wait_for_file = S3KeySensor(
        task_id = "wait_for_file",
        aws_conn_id = "aws_default",
        bucket_key = "s3://tomek_airflow/data*",
        wildcard_match = True
    )

    @task
    def process_file():
        print("Processed the file!")

    wait_for_file >> process_file()

aws_s3_dag()