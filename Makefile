.PHONY: help
help:  ## Show this help menu
	@echo "Usage: make [TARGET ...]"
	@echo ""
	@grep --no-filename -E '^[a-zA-Z_%-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-25s %s\n", $$1, $$2}'

VENV           = .venv
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(shell which python3.12)
PYTHON         = $(wildcard $(VENV_PYTHON))

$(VENV_PYTHON):
	rm -rf $(VENV)
	$(SYSTEM_PYTHON) -m venv $(VENV)

.PHONY: venv
venv: $(VENV_PYTHON)  ## Create a Python venv

.PHONY: deps
deps:  ## Install deps in venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install --no-cache-dir -r requirements.txt

.PHONY: fmt
fmt:  ## Format code
	$(PYTHON) -m yapf --recursive --exclude '.venv' --in-place .
