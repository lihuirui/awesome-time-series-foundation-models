.PHONY: fetch validate count readme help

PYTHON ?= python3

help:
	@echo "Targets: fetch | validate | count | readme"

fetch:
	$(PYTHON) scripts/fetch_arxiv.py

validate:
	$(PYTHON) scripts/validate.py

count:
	$(PYTHON) -c "import json; d=json.load(open('data/papers.json')); print(len(d['papers']))"

readme:
	$(PYTHON) scripts/generate_readme.py
