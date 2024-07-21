
pyenv:
	pyenv virtualenv 3.9.2 fast-3.9.2
	pyenv activate fast-3.9.2

build:
	pip3 install -r requirements.txt

start:
	uvicorn main:app --reload

migration:
	@read -p "Enter migration message:" message; \
	alembic revision --autogenerate -m "$$message"

migrate:
	alembic upgrade head