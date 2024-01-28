default: most

all:  most current demo test mutmut pyanalyse XXX missing todo mypy_all
most:      current      test mutmut pyanalyse             todo mypy_now

include Mk/RPy.mk

# LAST: 	Just finisched test, should still pass
# CURRENT:	The now current test, in TDD phase
# TODO:		Some test that are needed soon
rPY_LAST = \
	pytst/aigr/test_3_namespaces.py				\
	pytst/TD_AIGR/test_2_sieve_NS.py			\
#
rPY_CURRENT = \
	pytst/writers/RPy/test_3_SieveProtocols.py		\

#
CC2CPy_TODO = \
	pytst/aigr/test_3_namespaces.py				\
	pytst/aigr/test_0_AIGR.py				\
	pytst/writers/RPy/test_4_NameSpaces.py			\
	pytst/writers/RPy/test_99_SieveMoats.py			\
	pytst/writers/RPy/test_999.py 				\
#

include Mk/settings.mk
include Mk/testing.mk
include Mk/helpful.mk
include Mk/pyanalyse.mk
include Mk/mypy.mk

GAM: clean_generated current-only diff_TestDoubles

missing: missing_visitor missing_serialization
open:    coverage-open mutmut-open
remake:  veryclean coverage mutmut open

diff_TestDoubles:
	diff -w -rs  -x _keepThisDir -x .DS_Store TestDoubles/reference/ TestDoubles/_generated/

clean_generated:
	rm -f TestDoubles/_generated/*.{py,rpy} TestDoubles/_generated/*/*.{py,rpy}

clean_caches:
	find . -type d -name __pycache__    -print0 | xargs -0  rm -r
	find . -type d -name .pytest_cache  -print0 | xargs -0  rm -r
	rm -rf ./.coverage
	rm -rf ./.mutmut-cache
	rm -rf ./.mypy_cache

clean: clean_caches

cleaner: clean
	rm -rf ${COVERAGE_dir}
	rm -rf ${MUTMUT_dir}
	rm -rf ${PYREVERSE_DIR}*

cleanest veryclean: cleaner clean_generated

