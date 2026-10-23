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
#
CURRENT = \
	pytst/d03_support_classes/bundler/test_3_shallBundle.py
#
TODO = \
	pytst/d50_TESTDOUBLES/	\
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

