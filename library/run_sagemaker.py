#!/usr/bin/python
import boto3
from ansible.module_utils.basic import AnsibleModule


def build_training_job(
    aws_access_key,
    aws_secret_access_key,
    security_token,
    training_image="625399435531.dkr.ecr.eu-west-1.amazonaws.com/demo-sagemaker:latest",
    s3_output_path="s3://demo-sagemaker-artifacts/",
):
    client = boto3.client(
        "sagemaker",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=security_token,
    )
    training_job = client.create_training_job(
        TrainingJobName="demo-sagemaker-job",
        AlgorithmSpecification={
            "TrainingImage": training_image,
            "TrainingInputMode": "File",
        },
        RoleArn="arn:aws:iam::625399435531:role/SageMakerDefaultRole",
        OutputDataConfig={"S3OutputPath": s3_output_path},
        ResourceConfig={
            "InstanceType": "ml.m4.xlarge",
            "InstanceCount": 1,
            "VolumeSizeInGB": 20,
        },
        StoppingCondition={"MaxRuntimeInSeconds": 1200},  # 20mn
        Tags=[{"Key": "demo", "Value": "sagemaker"}],
    )
    return training_job


def run_training_job():

    module_args = dict(
        aws_access_key=dict(type="str"),
        aws_secret_key=dict(type="str"),
        security_token=dict(type="str"),
        training_image=dict(type="str"),
        s3_output_path=dict(type="str"),
    )

    module = AnsibleModule(
        argument_spec=module_args,
    )

    response = build_training_job(
        module.params["aws_access_key"],
        module.params["aws_secret_key"],
        module.params["security_token"],
        module.params["training_image"],
        module.params["s3_output_path"],
    )

    module.exit_json(**response)


if __name__ == "__main__":
    run_training_job()
