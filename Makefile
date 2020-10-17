install:
	@poetry install

lint:
	@poetry run flake8 gendiff/

selfcheck:
	@poetry check


check:	
	@selfcheck test lint


build: check
	@poetry build

.PHONY: install test lint selfcheck check build
