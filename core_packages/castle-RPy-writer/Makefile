default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writer			\
#
LAST = \
	pytst/test_dummy.py	\
	pytst/CC/  			\
	pytst/aid/ 			\
	pytst/transformers/	\
	pytst/translators/	\
	pytst/visitors/		\
	pytst/writer/		\
	pytst/HelloWorlds/test_02_Method.py \
	pytst/HelloWorlds/test_03_Call.py	\
	pytst/HelloWorlds/test_05_ComponentImplementation.py	\
	pytst/HelloWorlds/test_06_implicietComp.py	\
#
CURRENT = \
	pytst/machinery/ \
	pytst/HelloWorlds/test_12_file.py \
#
TODO = \
	pytst/HelloWorlds/test_05_ComponentImplementation.py
#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

