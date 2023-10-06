default: most

all:  most current demo test mutmut pyanalyse XXX missing todo
most:      current      test mutmut pyanalyse             todo

NOTES: CC2CpyNote
include Mk/RPy.mk

# LAST: 	Just finisched test, should still pass
# CURRENT:	The now current test, in TDD phase
# TODO:		Some test that are needed soon
rPY_LAST = \
	pytst/aigr/test_0_AIGR.py				\
	pytst/writers/RPy/test_1_EventIndexes.py		\
	pytst/aigr/test_2a_protocolKind.py			\
	pytst/aigr/test_2b_protocol.py				\
	pytst/writers/RPy/test_0_templating.py			\
	pytst/writers/RPy/test_1_EventIndexes.py		\
	pytst/writers/RPy/test_2_ProtocolDataStructures.py	\
	pytst/aigr/test_2c_GenericProtocols.py			\
	pytst/aigr/test_0_aid.py				\
#
rPY_CURRENT = \
	pytst/writers/RPy/test_99_SieveMoats.py			\
#
CC2CPy_TODO = \
	pytst/writers/RPy/test_999.py 				\
#

include Mk/settings.mk
include Mk/testing.mk
include Mk/helpful.mk

missing: missing_visitor missing_serialization
open:    coverage-open mutmut-open
remake:  veryclean coverage mutmut open

diff_TestDoubles:
	diff -w -rs TestDoubles/reference/ TestDoubles/_generated/

clean_generated:
	rm -f TestDoubles/_generated/*.{py,rpy} TestDoubles/_generated/*/*.{py,rpy}

clean_caches:
	find . -type d -name __pycache__    -print0 | xargs -0  rm -r
	find . -type d -name .pytest_cache  -print0 | xargs -0  rm -r
	rm -f ./.coverage
	rm -f ./.mutmut-cache

clean: clean_caches

cleaner: clean
	rm -rf ${COVERAGE_dir}
	rm -rf ${MUTMUT_dir}
	rm -rf ${PYREVERSE_DIR}*

cleanest veryclean: cleaner clean_generated

#CC2Cpy is outdated -- see make CC2CpyNote
include mk/CC2Cpy.mk
