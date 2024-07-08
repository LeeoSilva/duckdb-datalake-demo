.PHONY: docs create-network dev gen-sftp up-sftp up-airflow up-sftp up-airflow


docs: 
	poetry run python diagram.py

create-network: # create only if it doesn't exist
	docker network inspect datalake-gcp-demo >/dev/null 2>&1 || \
	docker network create --driver bridge datalake-gcp-demo

dev: 
	@$(MAKE) create-network
	@$(MAKE) up-airflow
	@$(MAKE) up-sftp

gen-sftp: 
	docker exec -it datalake-gcp-demo-airflow-triggerer-1 openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout /tmp/test_rsa.key

up-sftp: 
	@$(MAKE) gen-sftp
	docker exec -it datalake-gcp-demo-airflow-triggerer-1 sftpserver --host=localhost -p 2222 -k /tmp/test_rsa.key

up-airflow: 
	docker compose up -d 


