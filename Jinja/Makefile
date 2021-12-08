default: demos

all: demos tst
rTOPd = ../../.

DEMOS:=$(wildcard demo/*demo*.py)
demos:
	for d in ${DEMOS}; do echo "*** $$d ***";  python $$d; done
tst:
	(cd pytst/; pytest)
tst-s:
	(cd pytst/; pytest -s)

find_dot:
	find ${rTOPd} -iname \*.dot

clean:
	rm -f *.dot
	rm -f pytst/*.dot
