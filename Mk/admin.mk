# (C) Albert Mietus, 2025. Part of Castle/CCastle project

find_Makefiles:
	find . -type f -iname Makefile | fgrep -v ./Makefile | sort

SUBS ?=.
XXX ToDo Really hack HACK :
	-! grep -i $@ `find ${SUBS} -type f -iname \*.py` /dev/null # Reverse and ignore error-code

AssertFalse assertFalse assertfalse:
	-@ grep -i -E 'assert +False' `find . -type f -iname \*.py \! -iname test_\* ` /dev/null

show: XXX ToDo Really hack HACK AssertFalse

_sync-bookmarks:
	for b in $$(hg branches | awk '{print $$1}'); do \
	    hg bookmark -r "$$b" "$$b"; \
	done

push-all: _sync-bookmarks
	-hg push
	-hg push github
	-hg bookmark default
	-hg push github
	-hg push
