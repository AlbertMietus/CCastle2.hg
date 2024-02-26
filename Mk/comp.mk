
# SET in each <comp>/Makefile
#
## dirs
#
### TOPd:
##### - the rpath to "this dir": .../Mk/
##### - It ends with a '/'!
#
## marco's
## (list of files)
### LAST: 	Just finisched test, should still pass
### CURRENT:	The now current test, in TDD phase
### TODO:	Some tests that are needed soon



include ${TOPd}Mk/settings.mk
include ${TOPd}Mk/testing.mk
include ${TOPd}Mk/pyanalyse.mk
include ${TOPd}Mk/mypy.mk
include ${TOPd}Mk/clean.mk

all:	${ALL}


doc:; echo #No DOCS, for now
