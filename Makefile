.PHONY: clean
clean:
	rm -rf .venv build dist **/*.egg-info .pytest_cache node_modules .coverage


.PHONY: postgres
postgres:
	docker run -d -p 5432:5432 --name meu-postgres postgresql_db:lastest
	sleep 10
	python3 postgresql/create_table.py

.PHONY: install
install: ## Install the project dependencies and pre-commit using Poetry.
	poetry install --with test,lint
	poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push

.PHONY: run
run:
	cd dbt_project && dbt run

.PHONY: init
init: clean postgres install
