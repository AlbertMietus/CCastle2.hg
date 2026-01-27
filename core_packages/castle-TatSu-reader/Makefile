default: all


PYREVERSE_PKGS = \
	castle.readers \
	castle.readers.parser \
#
LAST = \
	pytst/parse/d01_simple/ \
	pytst/parse/test_4a_EH.py    \
	pytst/parse/test_5_meta.py  \
	pytst/parse/test_4b_method.py \
#
CURRENT = \
	pytst/parse/d05_statements/test_1_voidCall.py
#
TODO = \
	pytst/HW/test_1_elemental.py    \
	pytst/parse/test_9a_comp_implement.py \
	pytst/parse/test_9b_comp_mix.py\
#

DoH DOH Dot-On-Horizon:
	pytest --runxfail --capture=no  pytst/HW/test_1_elemental.py
DoH-info DOH-info:
	pytest --runxfail --log-cli-level=INFO pytst/HW/test_1_elemental.py
DoH-ds DOH-ds:
	pytest --runxfail  -rxXsfE  --log-cli-level=DEBUG -s pytst/HW/test_1_elemental.py

TOPd=../../
include ${TOPd}Mk/comp.mk

