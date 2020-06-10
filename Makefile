runserver:
	python manage.py runserver
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
shell_plus:
	python manage.py shell_plus
flake:
	flake8 .
tests:
	pytest
testads:
	pytest shop/tests/test_ads.py
clean-python:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;
djangosettings:
	export DJANGO_SETTINGS_MODULE=liteshop.settings
