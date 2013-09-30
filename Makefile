lazy:
	grep -r TODO resourceprovider --exclude=*.pyc

todo:
	grep -r "raise NotImplementedError" resourceprovider --exclude=*.pyc

test:
	dukaan manifest
	dukaan create
	dukaan show
	dukaan upgrade
	dukaan sso

init:
	python init.py
	dukaan init

dev:
	python manage.py development

prod:
	python manage.py production

pep:
	autopep8 -i -r resourceprovider
	autopep8 -i -r tests