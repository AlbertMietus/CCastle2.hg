default: all

all: demo test missing

missing: missing_visitor missing_serialization

PYTEST_OPTONS=-rxXsfE
pytest test:
	pytest ${PYTEST_OPTONS}  pytst/
pytest-s test-s:
	pytest ${PYTEST_OPTONS} -s pytst
test-ds test-sd test-d:
	pytest ${PYTEST_OPTONS} --log-cli-level=DEBUG -s pytst/
demo:
	pytest -s demos
	@echo run other demos by hand


missing_visitor: castle/readers/parser/grammar.py
	@for R in $(shell grep '^ *def ' $<  | awk '{print $$2}' | sed 's/()://') ; do	\
	        if !  grep -q -E "^ *((def)|(# *NO_VISITOR_NEEDED:)) *visit_$$R" castle/readers/parser/visitor.py > /dev/null ; then\
			echo "Warning: $${R} has no visitor (nor is marked as to need none)" ;\
		fi ;\
	done
QAZ := ${shell grep '^ *class ' castle/ast/peg.py | sed 's/class //g' | sed 's/[:( ].*$$//g' }
missing_serialization:
	@for R in ${QAZ} ; do \
	        if !  grep -q -E "^ *((def)|(# *NO_VISITOR_NEEDED:)) $${R}2xml" castle/ast/serialization.py > /dev/null ; then\
			echo "Warning: $${R} has no xml-serializer (nor is marked as to need none)" ;\
		fi ;\
	done
