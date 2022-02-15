default: all

all: demo test XXX missing

missing: missing_visitor missing_serialization

PYTEST_OPTONS=-rxXsfE
pytest test:
	pytest ${PYTEST_OPTONS}  pytst/
pytest-s test-s:
	pytest ${PYTEST_OPTONS} -s pytst
test-ds test-sd test-d:
	pytest ${PYTEST_OPTONS} --log-cli-level=DEBUG -s pytst/

demo: pytest-demo python-demo

python-demo:
	@echo Running all 'dem*.py' python-files
	export PYTHONPATH=`pwd`; for d in `find demos -type f -iname \*.py `; do echo "=== $$d ==="; python $$d; echo "=========="; done

pytest-demo:
	PYTHONPATH=`pwd` pytest -s demos


missing_visitor: castle/readers/parser/grammar.py
	@for R in $(shell grep '^ *def ' $<  | awk '{print $$2}' | sed 's/()://') ; do	\
	        if !  grep -q -E "^ *((def)|(# *NO_VISITOR_NEEDED:)) *visit_$$R" castle/readers/parser/visitor.py > /dev/null ; then\
			echo "Warning: $${R} has no visitor (nor is marked as to need none)" ;\
		fi ;\
	done

missing_serialization:
	@for R in ${shell grep '^ *class ' castle/ast/peg.py | sed 's/class //g' | sed 's/[:( ].*$$//g' } ; do \
	        if !  grep -q -E "^ *((def)|(# *NO_VISITOR_NEEDED:)) $${R}2xml" castle/ast/ast2xml.py > /dev/null ; then\
			echo "Warning: $${R} has no xml-serializer (nor is marked as to need none)" ;\
		fi ;\
	done
XXX:
	grep XXX `find . -type f -name \*.py`

clean: clean_caches
clean_caches:
	find . -type d -name __pycache__    -print0 | xargs -0  rm -r
	find . -type d -name .pytest_cache  -print0 | xargs -0  rm -r
