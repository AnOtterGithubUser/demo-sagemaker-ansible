# Seamless cloud experience

version: 0.1.0

This project aims at making training a model on the cloud as easy as in your local environment. 
For now, the models are trained on AWS SageMaker. The main dependencies are Docker and Ansible. This approach is agnostic 
of your machine learning framework.  
  
### Quick start

Clone this repository and run `pip install -r requirements.txt`, preferably in a virtual environment.  
Then, write your AWS credentials in `vault/credentials.yml` and the path to your python environment executable in `group_vars/all/vars.yml`.  
Put all your application code for training in `application`.  
You will need a role with access to AWS SageMaker, AWS ECR, and AWS S3. You can create it yourself in AWS IAM 
or ask your organization to do it. You will need to specify the ARN and name of this role into `group_vars/all/vars.yml`.  
Once you are done with that, simply run `make run-playbook`
  
### Functioning

This project uses Ansible and Docker to leverage AWS SageMaker training.  
When running `make run-playbook`, the code in `application/` is copied into a docker with a pre-installed version of TensorFlow,
 compiled for SageMaker. This docker image is sent to AWS Elastic Container Registry. AWS SageMaker will then pull the image 
 from the registry and run `train.py` in `application/`. Ansible sends pings to SageMaker until the training job is completed. 
 Then it will copy the resulting artifacts into the path you specified in `DESTINATION_FOLDER` and `DESTINATION_FILE` in `group_vars/all/vars.yml`.
