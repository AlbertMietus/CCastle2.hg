default: all


PYREVERSE_PKGS = \
	castle.readers \
	castle.readers.parser \
#
LAST = \
	pytst/parse/test_4a_EH.py    \
	pytst/parse/test_1c_args.py \
	pytst/parse/test_5_meta.py  \
	pytst/parse/test_1d_comment.py \
	pytst/parse/test_1e_docstrings.py \
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
	pytest --runxfail  pytst/HW/test_1_elemental.py
DoH-ds HOH-ds:
	pytest --runxfail  -rxXsfE  --log-cli-level=DEBUG -s pytst/HW/test_1_elemental.py


TOPd=../../
include ${TOPd}Mk/comp.mk

