default: all

all: test missing_visitors

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

GRAMMAR_RULES := $(shell grep '^ *def ' ./grammar.py | awk '{print $$2}' | sed 's/()://')

missing_visitors:
	@for R in ${GRAMMAR_RULES}; do	\
	        if !  grep -q -E "^ *((def)|(# *NO_VISITOR_NEEDED:)) *visit_$$R" ./visitor.py> /dev/null ; then\
			echo "Warning: $${R} has no visitor (nor is marked as to need none)" ;\
		fi ;\
	done

PYREVERSE_FORMAT=svg
PYREVERSEd=./pyreversed/

pyreverse : ${PYREVERSEd}
	pyreverse -d ${PYREVERSEd} -o ${PYREVERSE_FORMAT} -fALL -A  -my -p TryOut.Arpeggio 	grammar.py visitor.py 

