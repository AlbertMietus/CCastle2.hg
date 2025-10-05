default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle/writers/RPy					\
	castle/writers/RPy/CC				\
	castle/writers/RPy/writer			\
#
LAST = \
	pytst/HelloWorlds/test_05_ComponentImplementation.py \
	pytst/HelloWorlds/test_12_file.py \
#
CURRENT = \
	pytst/machinery/test_chain_dict.py \
#
TODO = \
	pytst/HelloWorlds/test_13_translate.py\
#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

