from airflow.sdk import chain, dag, task, Context

@dag 
def xcom_dag():
    @task
    def task_a(ti):
        val = {
            "value": 32,
            "message": "Hello from task_a!"    
        }
        ti.xcom_push(key="my_key", value=val)

    @task
    def task_c(ti):
        val = {
            "value": 34,
            "message": "Hello from task_c!"    
        }
        ti.xcom_push(key="my_key", value=val)


    @task
    def task_b(ti):
        val = ti.xcom_pull(key="my_key", task_ids="task_a")
        val2 = ti.xcom_pull(key="my_key", task_ids="task_c")
        print(f"Value from task_a: {val}")
        print(f"Value from task_c: {val2}")
    
    chain(task_a(), task_c(), task_b())

xcom_dag()