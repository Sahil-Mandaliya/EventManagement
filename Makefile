COMMIT_ID := `git rev-parse --short HEAD`

.PHONY: install
install:
	make pyenv
	make precommit
	make build

.PHONY: pyenv
pyenv:
	pyenv install 3.9.2
	pyenv virtualenv 3.9.2 event-api-3.9.2
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: build
build:
	docker-compose -f ./docker-compose.yml build event-management-service

# Starts the api service
.PHONY: start
start:
	docker-compose -f ./docker-compose.yml up -d
	docker-compose -f ./docker-compose.yml ps


.PHONY: migration
migration:
	docker-compose -f ./docker-compose.yml run --rm event-management-service alembic revision --autogenerate -m "Auto-generated migration"


.PHONY: migrate
migrate:
	docker-compose -f ./docker-compose.yml run --rm event-management-service alembic upgrade head

migrations-downgrade:
	docker-compose -f ./docker-compose.yml run --rm event-management-service alembic downgrade -1


.PHONY: precommit
precommit:
	pre-commit install

.PHONY: superuser
create-superuser:
	docker-compose exec event-management-service python /app/create_superuser.py --username $(USERNAME) --password $(PASSWORD) --email $(EMAIL) --full_name $(FULL_NAME) --phone $(PHONE)