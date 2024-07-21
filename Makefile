
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
	pip3 install -r requirements.txt

.PHONY: start
start:
	uvicorn main:app --reload

.PHONY: migration
migration:
	@read -p "Enter migration message:" message; \
	alembic revision --autogenerate -m "$$message"

.PHONY: migrate
migrate:
	alembic upgrade head

.PHONY: precommit
precommit:
	pre-commit install