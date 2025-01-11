default: all

PYREVERSE_PKGS = \
	castle.aigr \
	\
	castle.aigr.base \
	castle.aigr.expressions \
	castle.aigr.machinery \
	castle.aigr.statements \
	\
	castle.aigr_extra \
	castle.aigr_extra.blend \
	castle.aigr_extra.builders \
	\
	castle.aigr.namespaces

#

LAST = \
	pytst/base/test_ID.py					\
	pytst/statements/test_components.py 	\
	pytst/test_3_namespaces.py				\
#
CURRENT = \
	pytst/test_scope.py						\
#
TODO = \
	pytst/expressions/test_literals.py 		\
	pytst/test_3_namespaces.py				\
	pytst/machinery/test_9_todo.py			\
#

TOPd=../../
include ${TOPd}Mk/comp.mk

DATE:=`date "+%Y%m%d"`
_FILE_base := _pyreversed/classes_castle_aigr-noModules
_FILE_in   := ${_FILE_base}.plantuml
_FILE_tmp  := _pyreversed/classes_castle_aigr-DATE.svg
_FILE_out  := _pyreversed/classes_castle_aigr-${DATE}.svg
patch-doc doc-patch:
	@echo "patching '_pyreversed/classes_castle_aigr-noModules' to added packages"
	patch -p0  ${_FILE_in} < etc/plantuml-aigr-classes-visual.patch
	plantuml -tsvg ${_FILE_in}
	mv ${_FILE_tmp} ${_FILE_out}
	open ${_FILE_out}


