default: tst

all:  tst demos

DEMOS:=$(wildcard demo/*demo*.py)
demos:
	for d in ${DEMOS}; do echo "*** $$d ***";  python $$d; done
tst:
	(cd pytst/; pytest)
tst-s:
	(cd pytst/; pytest -s)


clean:
	rm -rf {.,castle}/{__pycache__,.pytest_cache}/
	rm -rf pytst/{.,*}/{__pycache__,.pytest_cache}/
	rm -f *.dot
	rm -f pytst/*.dot

