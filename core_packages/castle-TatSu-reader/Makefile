default: all


PYREVERSE_PKGS = \
	castle.readers \
	castle.readers.parser \
#
LAST = \
	pytst/d1_parse/d03_callable/test_4b_method.py \
	pytst/d2_HW/test_1_elemental.py
#
CURRENT = \
	pytst/d1_parse/d05_comp/test_6_InterfaceImplementMix.py\
#
TODO = \
	pytst/d1_parse/d06_meta/test_99_todo.py\
#

DoH DOH Dot-On-Horizon:
	pytest --runxfail --capture=no  pytst/d02_HW/test_1_elemental.py
DoH-info DOH-info:
	pytest --runxfail --log-cli-level=INFO pytst/d02_HW/test_1_elemental.py
DoH-ds DOH-ds:
	pytest --runxfail  -rxXsfE  --log-cli-level=DEBUG -s pytst/d02_HW/test_1_elemental.py

TOPd=../../
include ${TOPd}Mk/comp.mk

