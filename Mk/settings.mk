ToCS_dir     = _ToCS-reports/
COVERAGE_dir = ${ToCS_dir}Coverage/
MUTMUT_dir   = ${ToCS_dir}MutMut/

PYREVERSE_dir 	 = _pyreversed/
PYREVERSE_FORMAT = svg

SETS	= last current-only current todo current-ds current-info
TYPICAL = all clean cleaner cleanest veryclean doc test build
ALL	= current last todo pyanalyse todo mypy build
TEST 	= test pytest coverage mutmut
FULL	= ${SETS} ${TYPICAL} ${ALL} ${TEST}
