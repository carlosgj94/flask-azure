lazy:
	grep -r TODO resourceprovider --exclude=*.pyc
	grep -r "raise NotImplementedError" tests --exclude=*.pyc

todo:
	grep -r "raise NotImplementedError" resourceprovider --exclude=*.pyc

test:
	python tests/__init__.py

init:
	python init.py

dev:
	python manage.py development

prod:
	python manage.py production

pep:
	autopep8 -i -r resourceprovider
	autopep8 -i -r tests