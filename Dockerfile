FROM 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:2.3.0-cpu-py37-ubuntu18.04

COPY application/* .

RUN pip install -r requirements.txt

