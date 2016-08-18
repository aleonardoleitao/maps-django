install:
	@pip install -r requirements.txt


install-dev: install
	@pip install -r requirements-dev.txt


run:
	@python manage.py runserver --settings localidades.settings.dev


expose:
	@python manage.py runserver --settings localidades.settings.dev 0.0.0.0:8000


clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf


test: clean
	@python manage.py test --settings localidades.settings.test


fetch-db-dump:
	#@echo Downloading dump..
	#@curl -s -O http://infranm.globosat.net.br/bancodedados/dumps/riomp95lb01/svc_notificacao_django.gz
	#@echo Unpacking..
	#@gunzip -f svc_notificacao_django.gz
	@echo Applying to local database..
	@mysql -u root -e "drop database if exists svc_maps_django; create database svc_maps_django;"
	#@mysql -u root svc_notificacao_django < svc_notificacao_django
	#@rm svc_notificacao_django
	#@python manage.py migrate
