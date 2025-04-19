default: all

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writers			\
#
LAST = \
	pytst/HelloWorlds/test_12_file.py						\
#
CURRENT = \
	pytst/translators/test_0.py
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

