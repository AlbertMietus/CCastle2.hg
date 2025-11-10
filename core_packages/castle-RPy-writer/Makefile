default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle/writers/RPy_buildin		\
	castle/writers/RPy				\

#
LAST = \
	pytst/d11_HelloWorlds/d1_elemental/ 	\
	pytst/d04_render/test_7_Proto.py	\
	pytst/d04_render/test_6_Comp.py \
#
CURRENT = \
	pytst/d03_RPy/machinery/test_event.py
#
TODO = \
	pytst/d11_HelloWorlds/d2_credible/test_12_file.py::test_1_renderToTxt \
	pytst/d11_HelloWorlds/d2_credible/test_12_file.py \
#

HW_Ed = TestDoubles/HelloWorlds/elemental

all: demo

demo out clean_out clean:
	make -C  ${HW_Ed} $@

TOPd=../../
include ${TOPd}Mk/comp.mk

all: new
new:
	@@echo "The following elements are new (in credible but not in elemental):"
	@echo EventProtocol, Event
	@echo aigr.Def aigr.Ref
	@echo aigr.TypedParameter
	@echo aigr.types.string
	@echo aigr.Port, aigr.PortDirection.In
	@echo aigr.Constant
	@echo aigr.VariableDefintion
	@echo aigr.Become
	@echo aigr.machinery.sendEvent
	@echo aigr.Argument
	@echo aigr.Constant
	@echo aigr.Initializer
