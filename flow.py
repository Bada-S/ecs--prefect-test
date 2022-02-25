from prefect import Flow, task
from prefect.storage import S3
from prefect.run_configs.ecs import ECSRun


@task
def do_something():
    return 1 + 1


with Flow(
    name="ECS-run",
    run_config=ECSRun(task_definition_path="s3://coiled-prefect/task_defintion.yaml"),
    storage=S3(bucket="coiled-prefect"),
) as flow:
    do_something()

if __name__ == "__main__":
    flow.run(run_on_schedule=False)
