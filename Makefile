
pyenv:
	pyenv virtualenv 3.9.2 fast-3.9.2
	pyenv activate fast-3.9.2

build:
	make pyenv
	pip3 install -r requirements.txt

start:
	uvicorn app.main:app --reload

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate