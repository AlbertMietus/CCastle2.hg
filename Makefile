default: all

all: current demo test mutmut pyanalyse XXX missing current-todo
NOTES: CC2CpyNote

include Mk/RPy.mk
rPY_LAST = \
	pytst/writers/rPY/XXX					\
#
rPY_CURRENT = \
	pytst/writers/rPY/XXX					\
#
CC2CPy_TODO = \
	pytst/writers/rPY/XXX					\
#

include Mk/settings.mk
include Mk/testing.mk
include Mk/helpful.mk

missing: missing_visitor missing_serialization
open:    coverage-open mutmut-open
remake:  veryclean coverage mutmut open

clean_caches:
	find . -type d -name __pycache__    -print0 | xargs -0  rm -r
	find . -type d -name .pytest_cache  -print0 | xargs -0  rm -r
	rm -f ./.coverage
	rm -f ./.mutmut-cache

cleaner: clean
	rm -rf ${COVERAGE_dir}
	rm -rf ${MUTMUT_dir}
	rm -rf ${PYREVERSE_DIR}*

cleanest veryclean: cleaner

#CC2Cpy is outdated -- see make CC2CpyNote 
include mk/CC2Cpy.mk
