from airflow.sdk import dag, task

@dag
def basic_branch():
    @task.branch
    def choose_branch(value: int):
        if value > 10:
            return "branch_a"
        else:
            return "branch_b"
    
    @task
    def branch_a():
        print("Branch A")
    
    @task
    def branch_b():
        print("Branch B")
    
    choose_branch(5) >> [branch_a(), branch_b()]
basic_branch()