default: all

PYREVERSE_PKGS = castle/writers/RPy

LAST = \
	pytst/ASIDE/	\
#
CURRENT = \
	pytst/ASIDE/test_0_templating/test_gen_basic_txt.py	\
#
TODO = \
	pytst/ASIDE/	\
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
