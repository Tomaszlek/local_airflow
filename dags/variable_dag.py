from airflow.sdk import dag, task, Variable
from pendulum import datetime

@dag
def variable_dag():
    @task
    def print_variable():
        my_variable = Variable.get("api", deserialize_json=True)
        print(f"The value of 'my_variable' is: {my_variable}")

    print_variable()
variable_dag()