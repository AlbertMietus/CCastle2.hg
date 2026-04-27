default: all

PYREVERSE_PKGS = \
	castle.aigr \
	\
	castle.aigr.base \
	castle.aigr.components \
	castle.aigr.expressions \
	castle.aigr.machinery \
	castle.aigr.statements \
	\
	castle.aigr_extra \
	castle.aigr_extra.blend \
	castle.aigr_extra.builders \
	castle.aigr.tools.scaffolding \
	\
#
LAST = \
	pytst/extra/scaffolding/test_1_scaffolding.py  \
	pytst/extra/scaffolding/test_ScaffolderBody.py \
	pytst/test_2b_protocol.py \
	pytst/test_2c_GenericProtocols.py \
	pytst/test_3_namespaces.py \
	pytst/base/test_RefID.py   \
#
CURRENT = \
	pytst/extra/scaffolding/test_search_qualNames.py
#
TODO = \
	pytst/machinery/test_9_todo.py \
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


