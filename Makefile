lazy:
	grep -r TODO resourceprovider

todo:
	grep -r "raise NotImplementedError" resourceprovider

test:
	python tests/__init__.py