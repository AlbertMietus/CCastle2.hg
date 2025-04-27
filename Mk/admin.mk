# (C) Albert Mietus, 2025. Part of Castle/CCastle project

find_Makefiles:
	find . -type f -iname Makefile | fgrep -v ./Makefile | sort

SUBS ?=.
XXX ToDo Really hack HACK :
	-! grep -i $@ `find ${SUBS} -type f -iname \*.py` /dev/null # Reverse and ignore error-code

show: XXX ToDo Really
