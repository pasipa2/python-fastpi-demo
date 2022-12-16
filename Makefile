build:
	docker-compose build

start:
	docker-compose up -d

check:
	sh test.sh

test:
	docker-compose exec web python -m pytest -v

cleanup:
	docker-compose down -v
