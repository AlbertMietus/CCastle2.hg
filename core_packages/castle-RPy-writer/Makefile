default: all

# XXX read from ./setup.py ??
PYREVERSE_PKGS = castle.writers.RPy

LAST = \
	pytst/test_0_templating.py			\
	pytst/test_1_EventIndexes.py 			\
	pytst/test_2_ProtocolDataStructures.py		\
#
CURRENT = \
	pytst/test_3_SieveProtocols.py			\
	pytst/test_4_NameSpaces.py			\
#

TODO = \
	pytst/test_99_SieveMoats.py			\
#



TOPd=../../
include ${TOPd}Mk/comp.mk

diff_TestDoubles:
	diff -w -rs  -x _keepThisDir -x .DS_Store pytst/TestDoubles/{reference/,_generated/}
