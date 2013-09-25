lazy:
	grep -r TODO resourceprovider --exclude=*.pyc

todo:
	grep -r "raise NotImplementedError" resourceprovider --exclude=*.pyc

test:
	python tests/__init__.py