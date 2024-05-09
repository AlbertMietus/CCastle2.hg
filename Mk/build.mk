build: all
	python -m build

install-e: build _install
install-fast: _install

#_install: _install-does-not-work
_install: _install-workaround

_install-does-not-work:
	pip install -e .  # does not work for mypy, use workaround
_install-workaround:
	echo "from setuptools import setup; setup()" >setup.py
	SETUPTOOLS_ENABLE_FEATURES="legacy-editable" pip install -e .
	rm setup.py

