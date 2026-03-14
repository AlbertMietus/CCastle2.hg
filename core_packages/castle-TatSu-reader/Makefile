default: all


PYREVERSE_PKGS = \
	castle.readers \
	castle.readers.parser \
#
LAST = \
	pytst/d01_parse/d03_callable/test_4b_method.py \
	pytst/d01_parse/d05_comp/test_9a_comp_implement.py \
#
CURRENT = \
	pytst/d02_HW/test_1_elemental.py
#
TODO = \
	pytst/\
#

DoH DOH Dot-On-Horizon:
	pytest --runxfail --capture=no  pytst/d02_HW/test_1_elemental.py
DoH-info DOH-info:
	pytest --runxfail --log-cli-level=INFO pytst/d02_HW/test_1_elemental.py
DoH-ds DOH-ds:
	pytest --runxfail  -rxXsfE  --log-cli-level=DEBUG -s pytst/d02_HW/test_1_elemental.py

TOPd=../../
include ${TOPd}Mk/comp.mk

