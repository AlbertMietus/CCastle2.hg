default: all

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writers			\

LAST = \
	pytst/CC/test_CCbuildin_1_prefix.py 					\
	pytst/aid/test_blocks.py								\
	pytst/visitors/test_walker.py							\
	pytst/HelloWorlds/test_1_fstring.py						\
	pytst/HelloWorlds/test_3_Call.py						\
	pytst/HelloWorlds/test_2_Method.py						\
#
CURRENT = \
	pytst/HelloWorlds/test_11_ComponentImplementation.py	\
#
TODO = \
	pytst/HelloWorlds/test_3_Call.py						\
	pytst/test_dummy.py		\
#

#local_test:: diff_TestDoubles

all: demo
demo: demo_HW_elemental

demo_HW_elemental:
	make -C TestDoubles/HelloWorlds/elemental demo

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
