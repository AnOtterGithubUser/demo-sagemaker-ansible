run-playbook:
	ansible-playbook -e @vault/credentials.yml train_model_on_sagemaker.yml -i inventories/inventory.ini -e ansible_python_interpreter=$$(which python)