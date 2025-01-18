default: all

#none:
	@echo "This dir needs work before ..."

PYREVERSE_PKGS = castle/writers/RPy

LAST = \
	pytst/test_dummy.py
#
CURRENT = \
	pytst/test_dummy.py
#
TODO = \
	pytst/test_dummy.py
#

#local_test:: diff_TestDoubles

TOPd=../../
include ${TOPd}Mk/comp.mk

TESTDOUBLESd = pytst/TestDoubles/
TESTDOUBLESd = pytst/ASIDE/TestDoubles/
diff_TestDoubles:
	diff -w -rs  -x _keepThisDir -x .DS_Store ${TESTDOUBLESd}{reference/,_generated/}

CLEAN_none-marker = ${TESTDOUBLESd}_nonefile_to-make-sure-there-is-always-afile-to-rm
clean_TestDoubles:
	@touch ${CLEAN_none-marker}
	rm `find  ${TESTDOUBLESd}_generated/ -type f -iname \*.rpy` ${CLEAN_none-marker}

local_clean_generated:: clean_TestDoubles
