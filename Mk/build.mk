# (C) Albert Mietus, 2025, 2026. Part of Castle/CCastle project

build-all: build build-tst

build: fast
	python -m build

install: build
	pip install -e .


###
### <*>-tst packages contain the (py)test file -- generate the pyproject file automatically.
###
PYPROJ-TST: dist_tst/pyproject.toml
dist_tst/pyproject.toml: pyproject.toml ${PYPROJ-TST_tool}
	python ${PYPROJ-TST_tool}

build-tst: dist_tst/pyproject.toml
	python -m build dist_tst/

install-tst: build-tst
	pip install dist_tst/dist/*.whl

