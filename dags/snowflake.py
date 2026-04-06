from airflow.sdk import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from pendulum import datetime

@dag()
def snowflake_dag():
    @task
    def print_message():
        print("Executing Snowflake DAG")

    execute_query = SQLExecuteQueryOperator(
        task_id='execute_snowflake_query',
        conn_id='snowflake_default',
        sql='SELECT CURRENT_VERSION();'
    )

    print_message() >> execute_query