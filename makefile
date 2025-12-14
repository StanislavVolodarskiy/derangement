.PHONY: help
help:
	cat makefile

.PHONY: clean
clean:
	find * -name '*.pyc' -delete
	find * -name __pycache__ -delete

.PHONY: setup
setup:
	pip install -r requirements.txt

.PHONY: test
test:
	flake8 derangement test* tools
	PYTHONPATH=. pytest --pdb -v -s --cov=derangement --cov-report=term-missing .

.PHONY: check_derangements
check_derangements:
	PYTHONPATH=. python tools/check_derangements.py
