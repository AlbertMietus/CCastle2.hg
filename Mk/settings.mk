# (C) Albert Mietus, 2025. Part of Castle/CCastle project

ToCS_dir     = _ToCS-reports/
COVERAGE_dir = ${ToCS_dir}Coverage/
MUTMUT_dir   = ${ToCS_dir}MutMut/

CONFIG_dir   = ${TOPd}config/
MUTMUT_cfg_d = ${CONFIG_dir}MutMut/

TOOLS_dir    = ${TOPd}tools/

CLASSTREE_tool  = ${TOOLS_dir}classtree.py
PYPROJ-TST_tool = ${TOOLS_dir}make_pyproject_tst.py



PYANALYSE_dir 	 = _pyanalyse/
PYREVERSE_FORMAT = plantuml


SETS	= last current current-ds current-info recheck
TYPICAL = all clean cleaner cleanest veryclean doc test pytest pytest-only
ALL	= current last todo pyanalyse todo mypy
BUILD	= ${ALL} build install installed
TEST 	= test pytest coverage mutmut fast pytest-html
OPENit	= coverage-open mutmut-open pyanalyse-open pytest-html-open
FULL	= ${SETS} ${TYPICAL} ${ALL} ${TEST} ${BUILD} ${OPENit}

full:	${FULL}

show_targets targets:
	awk '/^[A-Za-z][A-Za-z_ ]+:+/ { print $$1}' ${TOPd}mk/* | sort --ignore-case --unique
