default: all

PYFAST_OPTON=--fast

PYREVERSE_PKGS = \
	castle/writers/RPy_buildin		\
	castle/writers/RPy				\

#
LAST = \
	pytst/HelloWorlds/ \
#
CURRENT = \
	pytst/HelloWorlds/credible/	\
#
TODO = \
	pytst/
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
