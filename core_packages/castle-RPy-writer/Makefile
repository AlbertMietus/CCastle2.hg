default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle/writers/RPy				\
	castle/writers/RPy/transformers	\
	castle/writers/RPy/translators	\
	castle/writers/RPy/writer/machinery\
	castle/writers/RPy/writer		\
	castle/writers/RPy_buildin		\
	castle/writers					\

#
LAST = \
	pytst/d01_aid/\
	pytst/d03_RPy/\
	pytst/d06_RPy_buildin/\
	pytst/d04_render/test_1_ID.py 	\
	pytst/d04_render/test_6_Comp.py \
	pytst/d04_render/test_7_Proto.py\

#
CURRENT = \
	pytst/d03_RPy/machinery/test_0_Bundle.py\
#
TODO = \
	pytst/d04_render/test_5_ArgList.py\
	pytst/d03_RPy/machinery/test_event.py \
	pytst/d11_HelloWorlds/ \

#


HW_elemental = TestDoubles/HelloWorlds/elemental
HW_credible  = TestDoubles/HelloWorlds/credible/
all: demo

demo out clean_out clean:
	make -C  ${HW_elemental} $@
	make -C  ${HW_credible} $@

elemental:
	make -C  ${HW_elemental} all
credible:
	make -C  ${HW_credible} all


TOPd=../../
include ${TOPd}Mk/comp.mk

