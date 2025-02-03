.PHONY: init
init:
	pip install --upgrade pip tox pre-commit
	pip install --upgrade -e ".[technote,dev]"
	pre-commit install
	rm -rf .tox

.PHONY: clean
clean:
	rm -rf .tox
	rm -rf docs/api/*.rst
