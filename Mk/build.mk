# (C) Albert Mietus, 2025. Part of Castle/CCastle project

build: fast
	python -m build

install: build
	pip install -e .

installed:
	pip list| grep castle | sort

