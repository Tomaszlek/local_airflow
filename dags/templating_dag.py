from airflow.sdk import dag, task
from airflow.providers.standard.operators.python import PythonOperator
from pendulum import datetime

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    render_template_as_native_obj=True,
    tags=['templating']
)
def templating_dag():
    sum_nb = PythonOperator(
        task_id = 'sum_nb',
        python_callable=sum_numbers,
        op_args={{dag_run.conf["numbers"]}}
    )

templating_dag()