default: all


PYREVERSE_PKGS = \
	castle.readers \
	castle.readers.parser \
#
LAST = \
	pytst/d1_parse/d03_callable/test_4b_method.py \
	pytst/d5_HW/test_1_elemental.py
#
CURRENT = \
	pytst/d1_parse/d05_comp/test_6_InterfaceImplementMix.py\
#
TODO = \
	pytst/d1_parse/d06_meta/test_99_todo.py\
	pytst/d1_parse/d07_file/test_2_ns.py\
#

_DOH = \
	pytst/d5_HW/test_1_elemental.py\
	${TODO}\

DoH DOH Dot-On-Horizon:
	pytest --runxfail --capture=no  ${_DOH} 
DoH-info DOH-info:
	pytest --runxfail --log-cli-level=INFO  ${_DOH}
DoH-ds DOH-ds:
	pytest --runxfail  -rxXsfE  --log-cli-level=DEBUG -s  ${_DOH}

TOPd=../../
include ${TOPd}Mk/comp.mk

