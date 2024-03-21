default: all

# XXX read from ./setup.py ??
PYREVERSE_PKGS = castle.writers.RPy

LAST = \
	pytst/test_0_templating.py			\
	pytst/test_1_EventIndexes.py 			\
	pytst/test_2_ProtocolDataStructures.py		\
#
CURRENT = \
	pytst/test_3_SieveProtocols.py			\
	pytst/test_4_NameSpaces.py			\
#

TODO = \
	pytst/test_99_SieveMoats.py			\
#

local_test:: diff_TestDoubles

TOPd=../../
include ${TOPd}Mk/comp.mk

TESTDOUBLESd = pytst/TestDoubles/
diff_TestDoubles:
	diff -w -rs  -x _keepThisDir -x .DS_Store ${TESTDOUBLESd}{reference/,_generated/}

CLEAN_none-marker = ${TESTDOUBLESd}_nonefile_to-make-sure-there-is-always-afile-to-rm
clean_TestDoubles:
	@touch ${CLEAN_none-marker}
	rm `find  ${TESTDOUBLESd}_generated/ -type f -iname \*.rpy` ${CLEAN_none-marker}

local_clean_generated:: clean_TestDoubles
