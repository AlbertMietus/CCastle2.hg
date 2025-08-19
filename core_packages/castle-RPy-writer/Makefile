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
	pytst/HelloWorlds/test_02_Method.py \
	pytst/HelloWorlds/test_03_Call.py	\
	pytst/HelloWorlds/test_05_ComponentImplementation.py	\
	pytst/HelloWorlds/test_06_implicietComp.py	\
#
CURRENT = \
	pytst/visitors/test_walker.py::test_2_ComponentImplementation_has_2callables	\
	pytst/visitors/test_walker.py	\
	pytst/HelloWorlds/test_05_ComponentImplementation.py::test_4_full
#
TODO = \
	pytst/HelloWorlds/test_05_ComponentImplementation.py
	#pytst/HelloWorlds/test_12_file.py 		\
	#pytst/HelloWorlds/test_13_translate.py	\
	#pytst/HelloWorlds/test_07_eTable.py		\
	#pytst/writers/test_render_eDispatchTable.py 		\

#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

