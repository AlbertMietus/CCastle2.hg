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
	pytst/d03_RPy/machinery/test_01_PortrayType.py \
	pytst/d03_RPy/machinery/test_02_Bundler.py  \
	pytst/d03_RPy/machinery/test_02_Bundler.py  \
	pytst/d03_RPy/machinery/test_07_sync_Portray2buildin_names.py \
	pytst/d04_render/test_6_Comp.py \
	pytst/d04_render/test_7_Proto.py	\
	pytst/d04_render/test_7_Proto.py\
	pytst/d06_RPy_buildin/test_packValues.py \
	pytst/d11_HelloWorlds/d1_elemental/ 	\
#
CURRENT = \
	pytst/d03_RPy/machinery/test_11_bundler-simple.py \
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

