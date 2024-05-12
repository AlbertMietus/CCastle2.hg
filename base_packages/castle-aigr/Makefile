default: all

PYREVERSE_PKGS = castle/aigr \
	castle/aigr.machinery \
	castle/aigr.statements \
	castle/aigr.expressions \
	castle/aigr_extra.builders \
#

LAST = \
	pytst/statements/test_if.py		\
	pytst/statements/test_become.py		\
	pytst/expressions/test_callable.py	\
	pytst/expressions/test_compare.py	\
	pytst/expressions/test_LRbin.py		\
	pytst/expressions/test_LRmore.py	\
	pytst/expressions/test_RL.py		\
	pytst/statements/test_body.py		\
#
CURRENT = \
	pytst/statements/test_method.py 	\
	pytst/statements/test_components.py 	\
	pytst/statements/test_0_dataclass.py	\
	pytst/statements/test_0_kids.py		\
#
TODO = \
	pytst/test_3_namespaces.py		\
	pytst/machinery/test_9_todo.py		\
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


