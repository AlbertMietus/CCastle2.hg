default: all


PYREVERSE_PKGS = \
	castle.readers \
	castle.readers.parser \
#
LAST = \
	pytst/d01_parse/
#
CURRENT = \
	pytst/d01_parse/d07_file/test_1_loadFile.py\
#
TODO = \
	pytst/d02_HW/test_1_elemental.py    \
	pytst/d01_parse/d05_comp/test_9a_comp_implement.py \
	pytst/d01_parse/d05_comp/test_9b_comp_mix.py\
#

DoH DOH Dot-On-Horizon:
	pytest --runxfail --capture=no  pytst/d02_HW/test_1_elemental.py
DoH-info DOH-info:
	pytest --runxfail --log-cli-level=INFO pytst/d02_HW/test_1_elemental.py
DoH-ds DOH-ds:
	pytest --runxfail  -rxXsfE  --log-cli-level=DEBUG -s pytst/d02_HW/test_1_elemental.py

TOPd=../../
include ${TOPd}Mk/comp.mk

