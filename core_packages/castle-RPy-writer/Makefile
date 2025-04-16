default: all

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writers			\
#
LAST = \
	pytst/CC/test_CCbuildin_1_prefix.py 					\
	pytst/HelloWorlds/test_11_ComponentImplementation.py	\
	pytst/transformers/test_0.py							\
	pytst/transformers/test_1_toTargetNS.py					\
#
CURRENT = \
	pytst/HelloWorlds/test_12_file.py						\
#
TODO = \
	pytst/HelloWorlds/test_3_Call.py						\
	pytst/test_dummy.py		\
#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

