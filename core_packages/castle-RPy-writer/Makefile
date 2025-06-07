default: all

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writers			\
#
LAST = \
	pytst/HelloWorlds/test_06_implicietComp.py 		\
	pytst/CC/machinery/test_chainedDict.py				\
#
CURRENT = \
	pytst/writers/test_render_eDispatchTable.py 		\
#
TODO = \
	pytst/HelloWorlds/test_12_file.py 		\
	pytst/HelloWorlds/test_13_translate.py	\
#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

