FROM 763104351884.dkr.ecr.eu-west-1.amazonaws.com/tensorflow-training:2.3.0-cpu-py37-ubuntu18.04

# Copy requirements and training script to /opt/ml/code
COPY application/* /opt/ml/code/

# Install application requirements
RUN pip install -r /opt/ml/code/requirements.txt

ENTRYPOINT ["python", "/opt/ml/code/train.py"]
