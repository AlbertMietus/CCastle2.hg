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
	pytst/d01_aid/				\
	pytst/d02_simple_classes/	\
	pytst/d03_support_classes/	\
	pytst/d04_renderer/			\
	pytst/d20_buildin/			\
	pytst/d04_renderer/argList_bundling_variants/\
	pytst/d04_renderer/simple/test_4_Call_NoArgs.py\
	pytst/d04_renderer/argList_bundling_variants/test_callable_defs.py\
	pytst/d04_renderer/simple/test_5_CallArgs.py\
	pytst/d50_TESTDOUBLES/d5_HelloWorlds/d1_elemental/test_03_Call.py\
#
CURRENT = \
	pytst/d50_TESTDOUBLES/d5_HelloWorlds/d1_elemental/test_12_file.py::test_1_renderToTxt
#
TODO = \
	pytst/d50_TESTDOUBLES/d5_HelloWorlds/d1_elemental/	\
	pytst/d50_TESTDOUBLES/	\
#

#	pytst/d04_renderer/machinery/test_event.py # Not needed for elemental HelloWorld


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

