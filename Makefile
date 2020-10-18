install:
	@poetry install

lint:
	@poetry run flake8 gendiff/

selfcheck:
	@poetry check


check:	
	@test lint


build: check
	@poetry build

.PHONY: install test lint check build
