sub-build: all


include ${TOPd}Mk/recursive.mk

find_Makefiles:
	find . -type f -iname Makefile | fgrep -v ./Makefile | sort

XXX ToDo Really:
	-! grep $@ `find ${SUBS} -type f -iname \*.py` /dev/null # Reverse and ignore error-code

show: XXX ToDo Really


