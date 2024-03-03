build: all
	python -m build

install-e: build
	pip install -e .

