#!/usr/bin/python
import boto3
from ansible.module_utils.basic import AnsibleModule
import time


def get_monitored_job(training_job_summaries, training_job_arn):
    for job_summary in training_job_summaries:
        if job_summary["TrainingJobArn"] == training_job_arn:
            return job_summary
    return ValueError("Found no job with arn: %s" % training_job_arn)


def get_job_status(
    aws_access_key,
    aws_secret_access_key,
    security_token,
    training_job_arn,
    wait_between_tries=1,
    duration_threshold=360,
):
    client = boto3.client(
        "sagemaker",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=security_token,
    )

    completed = False

    start_time = time.time()
    while not completed:
        time.sleep(wait_between_tries)
        training_jobs = client.list_training_jobs(SortBy="CreationTime")
        try:
            job_to_monitor = get_monitored_job(
                training_jobs["TrainingJobSummaries"], training_job_arn
            )
        except ValueError:
            return {
                "TrainingJobArn": training_job_arn,
                "Status": "Error: Found no job with arn %s" % training_job_arn,
            }
        completed = job_to_monitor["TrainingJobStatus"] == "Completed"
        if time.time() - start_time > duration_threshold:
            return {
                "TrainingJobArn": training_job_arn,
                "Status": "Error: Exceeded maximum duration (%s s)"
                % duration_threshold,
            }

    return {"TrainingJobArn": training_job_arn, "Status": "Completed"}


def run_get_job_status():
    module_args = dict(
        aws_access_key=dict(type="str"),
        aws_secret_key=dict(type="str"),
        security_token=dict(type="str"),
        training_job_arn=dict(type="str"),
        wait_between_tries=dict(type="int"),
        duration_threshold=dict(type="int"),
    )

    module = AnsibleModule(
        argument_spec=module_args,
    )

    response = get_job_status(
        module.params["aws_access_key"],
        module.params["aws_secret_key"],
        module.params["security_token"],
        module.params["training_job_arn"],
        module.params["wait_between_tries"],
        module.params["duration_threshold"],
    )

    module.exit_json(**response)


if __name__ == "__main__":
    run_get_job_status()
