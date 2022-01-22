default: demos

all: demos test

test:
	(cd pytst/; pytest)
test-s:
	(cd pytst/; pytest -s)

DEMOS:=$(wildcard demo/*demo*.py)
demos:
	for d in ${DEMOS}; do echo "*** $$d ***";  python $$d; done

clean:
	rm -rf {.,castle}/{__pycache__,.pytest_cache}/
	rm -rf pytst/{.,*}/{__pycache__,.pytest_cache}/
	rm -f *.dot
	rm -f pytst/*.dot

PYREVERSE_FORMAT=svg
PYREVERSEd=./pyreversed/

pyreverse : ##${PYREVERSEd}
	#pyreverse -d ${PYREVERSEd} -o ${PYREVERSE_FORMAT} -fALL -A  -my -p TryOut.Jinja  ...
	@echo nothing yet
