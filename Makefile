.PHONY: install dev test example lint clean

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

test:
	pytest -q

example:
	python scripts/evaluate_candidate.py \
	  --problem examples/closed_form_constant \
	  --candidate examples/closed_form_constant/final/proposed_solution.py
	python scripts/evaluate_candidate.py \
	  --problem examples/graph_construction \
	  --candidate examples/graph_construction/final/proposed_solution.py

lint:
	python -m pyflakes src/math_harness || true

clean:
	rm -rf .pytest_cache **/__pycache__ *.egg-info build dist
