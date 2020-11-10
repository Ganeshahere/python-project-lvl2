install:
	@poetry install

lint:
	@poetry run flake8 gendiff/

selfcheck:
	@poetry check


check:	
	@test lint

test-with-coverage:
	poetry run pytest --cov=gendiff tests  --cov-report xml

build: check
	@poetry build

.PHONY: install test lint check build
