default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writers			\
#
LAST = \
	pytst/test_dummy.py	\
	pytst/CC/  			\
	pytst/aid/ 			\
	pytst/transformers/	\
	pytst/translators/	\
	pytst/visitors/		\
	pytst/writers/		\
#
CURRENT = \
	pytst/HelloWorlds/test_05_ComponentImplementation.py	\
#
TODO = \
	pytst/HelloWorlds/test_07_eTable.py		\
	pytst/HelloWorlds/test_12_file.py 		\
	pytst/HelloWorlds/test_13_translate.py	\
	pytst/writers/test_render_eDispatchTable.py 		\
	pytst/HelloWorlds/ \
#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

