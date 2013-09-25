lazy:
	grep -r TODO resourceprovider --exclude=*.pyc

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