default: all

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writers			\
#
LAST = \
	pytst/HelloWorlds/test_12_file.py 		\
	pytst/translators/test_0.py				\
#
CURRENT = \
	pytst/HelloWorlds/test_13_translate.py	\
#
TODO = \
	pytst/test_dummy.py					\
	pytst/HelloWorlds/test_3_Call.py 	\
#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

