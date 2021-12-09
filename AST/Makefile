default: test

all:  test demos

	(cd pytst/; pytest)
test-s:
	(cd pytst/; pytest -s)

DEMOS:=$(wildcard demo/*demo*.py)
demos:
	for d in ${DEMOS}; do echo "*** $$d ***";  python $$d; done
test:

clean:
	rm -rf {.,castle}/{__pycache__,.pytest_cache}/
	rm -rf pytst/{.,*}/{__pycache__,.pytest_cache}/
	rm -f *.dot
	rm -f pytst/*.dot

