up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

raw:
	docker exec -it lakehouse-jupyter python3 /home/jovyan/jobs/ingest_raw.py

silver:
	docker exec -it lakehouse-jupyter python3 /home/jovyan/jobs/build_silver.py

gold:
	docker exec -it lakehouse-jupyter python3 /home/jovyan/jobs/build_gold.py

postgres:
	docker exec -it lakehouse-jupyter python3 /home/jovyan/jobs/load_gold_to_postgres.py

pipeline:
	docker exec -it lakehouse-jupyter python3 /home/jovyan/jobs/run_pipeline.py

dbt-run:
	docker exec -it lakehouse-dbt dbt run --profiles-dir /usr/app

dbt-test:
	docker exec -it lakehouse-dbt dbt test --profiles-dir /usr/app

dbt-debug:
	docker exec -it lakehouse-dbt dbt debug --profiles-dir /usr/app

psql:
	docker exec -it lakehouse-postgres psql -U dbt -d warehouse