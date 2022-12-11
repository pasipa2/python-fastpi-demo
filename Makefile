build:
	docker-compose build

start:
	docker-compose up -d

check:
	curl http://localhost:8004/ping | json_pp

test:
	docker-compose exec web python -m pytest -v

cleanup:
	docker-compose down -v