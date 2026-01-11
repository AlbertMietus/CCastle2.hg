default: all


PYREVERSE_PKGS = \
	castle.readers \
	\
	castle.readers.parser \

#
LAST = \
	pytst/bootstrap/test_0a_bootstrap-tatsu.py \
	pytst/bootstrap/test_0b_bootstrap-tatsu_dict.py\
	pytst/parse/test_1b_parms.py \
	pytst/parse/test_1a_names.py \
	pytst/parse/test_3_comp_interface.py -k test_1a\
#
CURRENT = \
	pytst/parse/test_3_comp_interface.py -k test_1b\
#
TODO = \
	pytst/parse/test_3_comp_interface.py\
	pytst/parse/test_9a_comp_implement.py::test_3a_Comp_with_empty_EH\
	pytst/parse/test_9a_comp_implement.py\
#


TOPd=../../
include ${TOPd}Mk/comp.mk

