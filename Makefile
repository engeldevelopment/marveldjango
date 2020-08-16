run:
	@python manage.py runserver

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

test:
	@python manage.py test

coverage: lint
	@coverage run manage.py test
	@coverage report

lint:
	@flake8 marvel/

rm:
	@rm -rf htmlcov __pycache__ .coverage