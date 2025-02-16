ToCS_dir     = _ToCS-reports/
COVERAGE_dir = ${ToCS_dir}Coverage/
MUTMUT_dir   = ${ToCS_dir}MutMut/

CONFIG_dir   = ${TOPd}config/
MUTMUT_cfg_d = ${CONFIG_dir}MutMut/

PYREVERSE_dir 	 = _pyreversed/
PYREVERSE_FORMAT = plantuml


SETS	= last current current-ds current-info recheck
TYPICAL = all clean cleaner cleanest veryclean doc test pytest pytest-only
ALL	= current last todo pyanalyse todo mypy
BUILD	= ${ALL} build install-e install-fast
TEST 	= test pytest coverage mutmut
OPENit	= coverage-open mutmut-open pyanalyse-open
FULL	= ${SETS} ${TYPICAL} ${ALL} ${TEST} ${BUILD} ${OPENit}

