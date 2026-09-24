.PHONY: all check figures survey-check bibtex validate readme count fetch search help

PYTHON ?= python3

all: validate figures survey-check bibtex readme

check: validate survey-check

help:
	@echo "Targets: all | check | figures | survey-check | bibtex | validate | count | readme | fetch | search"

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

search:
	$(PYTHON) scripts/search_arxiv.py
