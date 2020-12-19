# Seamless cloud experience

version: 0.1.0

This project aims at making training a model on the cloud as easy as in your local environment. 
For now, the models are trained on AWS SageMaker. The main dependencies are Docker and Ansible. This approach is agnostic 
of your machine learning framework.  
  
### Quick start

git clone this repository and run `pip install -r requirements.txt`, preferably in a virtual environment.  
Then, write your AWS credentials in `vault/credentials.yml`. Put all your application code for training in `application`.  
You will need a role with access to AWS SageMaker, AWS ECR, and AWS S3. You can create it yourself in AWS IAM 
or ask your organization to do it. You will need to specify the ARN and name of this role into `group_vars/all/vars.yml`.  
Once you are done with that, simply run `make run-playbook`
