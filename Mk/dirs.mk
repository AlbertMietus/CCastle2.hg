sub-build: all


include ${TOPd}Mk/recursive.mk

find_Makefiles:
	find . -type f -iname Makefile | fgrep -v ./Makefile | sort


