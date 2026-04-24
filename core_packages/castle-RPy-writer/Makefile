default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle.writers.RPy_buildin		\
	castle.writers.RPy				\

#
LAST = \
	pytst/d04_render/test_7_Proto.py	\
	pytst/d04_render/test_6_Comp.py \
#
CURRENT = \
	pytst/d03_RPy/machinery/test_event.py
#
TODO = \
	pytst/d11_HelloWorlds/d1_elemental/test_13_translate.py					\
	pytst/d11_HelloWorlds/d2_credible/test_12_file.py::test_1_renderToTxt \
	pytst/d11_HelloWorlds/d2_credible/test_12_file.py \

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

