ToCS_dir     = _ToCS-reports/
COVERAGE_dir = ${ToCS_dir}Coverage/
MUTMUT_dir   = ${ToCS_dir}MutMut/

PYREVERSE_dir 	 = _pyreversed/
PYREVERSE_FORMAT = svg

SETS	= last current current-ds current-info recheck
TYPICAL = all clean cleaner cleanest veryclean doc test pytest pytest-only
ALL	= current last todo pyanalyse todo mypy
BUILD	= ${ALL} build
TEST 	= test pytest coverage mutmut
FULL	= ${SETS} ${TYPICAL} ${ALL} ${TEST}
