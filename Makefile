default: all

all: demo test pyanalyse XXX missing

missing: missing_visitor missing_serialization

PYTEST_OPTONS=-rxXsfE
pytest test coverage:
	coverage run --branch -m pytest ${PYTEST_OPTONS}  pytst/
	coverage report  --skip-covered
	coverage html
pytest-only:								# No coverage reports
	pytest ${PYTEST_OPTONS}  pytst
pytest-s:								# -s : No capure (so, show stdout/stderr)
	pytest ${PYTEST_OPTONS} -s pytst
pytest-d pytest-ds pytest-sd:						# with debuging
	pytest ${PYTEST_OPTONS} --log-cli-level=DEBUG -s pytst/

mutmut:									# Mutation testing (takes a long run) https://en.wikipedia.org/wiki/Mutation_testing
	-mutmut run  --tests-dir pytst --paths-to-mutate castle
	mutmut html ; mv html mutmut-report
	mutmut results
	open mutmut-report/index.html


demo: pytest-demo python-demo

python-demo:
	@echo Running all 'dem*.py' python-files
	export PYTHONPATH=`pwd`; for d in `find demos -type f -iname \*.py `; do echo "=== $$d ==="; python $$d; echo "=========="; done

pytest-demo:
	-PYTHONPATH=`pwd` pytest -s demos || echo "currently NO pytest-demos (check/fix manually)"

LANGUAGEd=castle/readers/parser/grammar/
missing_visitor: ${LANGUAGEd}language.py
	@for R in $(shell grep '^ *def ' $<  | awk '{print $$2}' | sed 's/()://') ; do \
		if !  grep -q -E "^ *((def)|(# *NO_VISITOR_NEEDED:)) *visit_$$R" ${LANGUAGEd}visitor.py > /dev/null ; then\
			echo "Warning: $${R} has no visitor (nor is marked as to need none)" ;\
		fi ;\
	done

ASTd=castle/ast/
missing_serialization: ${ASTd}grammar.py
	@for R in ${shell grep '^ *class ' $< | sed 's/class //g' | sed 's/[:( ].*$$//g' } ; do \
		if !  grep -q -E "^ *((def)|(# *NO_VISITOR_NEEDED:)) $${R}2xml" ${ASTd}serialization/ast2xml/*.py > /dev/null ; then\
			echo "Warning: $${R} has no xml-serializer (nor is marked as to need none)" ;\
		fi ;\
	done
XXX:
	grep XXX `find . -type f -name \*.py`

clean: clean_caches
clean_caches:
	find . -type d -name __pycache__    -print0 | xargs -0  rm -r
	find . -type d -name .pytest_cache  -print0 | xargs -0  rm -r
	rm -f ./.coverage
	rm -f ./.mutmut-cache

cleaner: clean
	rm -rd ./htmlcov/ #coverage
	rm -rf mutmut-report/ # mutmut

PYREVERSE_DIR=pyreversed
PYREVERSE_FORMAT=svg
PYREVERSE_OPTIONS=-kAmy
PYREVERSE_PRJS= castle castle.readers castle.ast #castle.writers

pyanalyse pyreverse: ${PYREVERSE_DIR}
	for P in ${PYREVERSE_PRJS}; do \
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYREVERSE_DIR} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P --colorized --max-color-depth=42 -my $$P >>/dev/null;\
		echo ".. done. Result-files:" ;\
		ls -l ${PYREVERSE_DIR}/*$${P}.${PYREVERSE_FORMAT} ;\
		echo;\
	done
