default: tst

all: tst
rTOPd = ../../.

tst:
	(cd pytst/; pytest)
tst-s:
	(cd pytst/; pytest -s)

find_dot:
	find ${rTOPd} -iname \*.dot

clean:
	rm -rf {.,castle}/{__pycache__,.pytest_cache}/
	rm -rf pytst/{.,*}/{__pycache__,.pytest_cache}/
	rm -f *.dot
	rm -f pytst/*.dot

