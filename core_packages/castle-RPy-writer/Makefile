default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle.writers					\
	castle.writers.RPy_buildin		\
	castle.writers.RPy				\
	castle.writers.RPy.transformers	\
	castle.writers.RPy.translators	\
	castle.writers.RPy.writer		\
	castle.writers.RPy.writer.machinery\
#

LAST = \
	pytst/d01_aid/	\
	pytst/d06_RPy_buildin/test_packValues.py \
	pytst/d04_render/test_5_ArgList.py				\
	pytst/d04_render/test_4_Call.py					\
	pytst/d06_RPy_buildin/test_0_CC_B_Values.py \
#
CURRENT = \
	pytst/d03_RPy/machinery/test_02_Bundler.py::test_5a_unpack_oneInt\
#
TODO = \
	pytst/d03_RPy/machinery \
	pytst/d11_HelloWorlds/d1_elemental/test_02_Method.py::test_2_full \
	pytst/d03_RPy/machinery/test_event.py \
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

