.PHONY: all figures survey-check bibtex validate readme count fetch help

PYTHON ?= python3

all: validate figures survey-check bibtex readme

help:
	@echo "Targets: all | figures | survey-check | bibtex | validate | count | readme | fetch"

validate:
	$(PYTHON) scripts/validate.py

figures:
	$(PYTHON) scripts/figures/generate_figures.py

survey-check:
	$(PYTHON) scripts/survey_check.py

bibtex:
	$(PYTHON) scripts/generate_bibtex.py

readme:
	$(PYTHON) scripts/generate_readme.py

count:
	$(PYTHON) -c "import json; d=json.load(open('data/papers.json')); print(len(d['papers']))"

fetch:
	$(PYTHON) scripts/fetch_arxiv.py
