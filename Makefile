default: all

all: current demo test mutmut pyanalyse XXX missing current-todo

LAST = \
	pytst/writers/CC2Cpy/test_2a_groundwork.py		\
	pytst/writers/CC2Cpy/test_2b_EventProtocol.py		\
	pytst/writers/CC2Cpy/test_3a_CompPort.py		\
	pytst/writers/CC2Cpy/test_3b_CompInterface.py		\
	pytst/writers/CC2Cpy/test_3c_CompClass.py		\
#
CURRENT_TESTS = \
	pytst/writers/CC2Cpy/test_3d_CompStruct.py 		\
	pytst/writers/CC2Cpy/test_9_genSieve.py			\
#
TODO_TESTS = \
	pytst/writers/CC2Cpy/test_999_NoNameCollision.py	\
#

ToCS_dir     = _ToCS-reports/
COVERAGE_dir = ${ToCS_dir}Coverage/
MUTMUT_dir   = ${ToCS_dir}MutMut/

missing: missing_visitor missing_serialization

PYTEST_OPTONS=-rxXsfE
pytest test coverage:
	coverage run --branch -m pytest ${PYTEST_OPTONS}  pytst/
	coverage report  --skip-covered
	coverage html --directory=${COVERAGE_dir}
coverage-open: coverage
	open ${COVERAGE_dir}index.html

pytest-only:								# No coverage reports
	pytest ${PYTEST_OPTONS}  pytst
pytest-s:								# -s : No capure (so, show stdout/stderr)
	pytest ${PYTEST_OPTONS} -s pytst
pytest-d pytest-ds pytest-sd:						# with debuging
	pytest ${PYTEST_OPTONS} --log-cli-level=DEBUG -s pytst/

mutmut: mutmut-3.11		    # Mutation testing (takes a long run) https://en.wikipedia.org/wiki/Mutation_testing
	-mutmut run  --tests-dir pytst --paths-to-mutate castle
	mutmut html && rm -rf ${MUTMUT_dir} && mv html ${MUTMUT_dir}
	mutmut results
mutmut-open: mutmut
	open ${MUTMUT_dir}index.html

mutmut-3.11:
	@echo Mutmut is currenly not working in python-3.11. See BUGS.rst.
	@echo But it works on 3.10 -- Therefore we use the 3.10 version
	python --version

open: coverage-open mutmut-open
remake: veryclean coverage mutmut open

last:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${LAST}
current-only:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${CURRENT_TESTS}
current:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${CURRENT_TESTS} ${TODO_TESTS}
current-todo:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${TODO_TESTS}
current-ds current-sd:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  --log-cli-level=DEBUG -s ${CURRENT_TESTS}


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

WC:
	wc -l `find . -type f -name \*.py`


PYREVERSE_DIR=pyreversed/
PYREVERSE_FORMAT=svg
PYREVERSE_OPTIONS=-k -A -my
PYREVERSE_PRJS= castle castle.readers castle.ast castle.writers.CC2Cpy

pyanalyse pyreverse: ${PYREVERSE_DIR}
	for P in ${PYREVERSE_PRJS}; do \
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYREVERSE_DIR} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P --colorized --max-color-depth=42 -my $$P >>/dev/null;\
		echo ".. done. Result-files:" ;\
		ls -l ${PYREVERSE_DIR}*$${P}.${PYREVERSE_FORMAT} ;\
		echo;\
	done

clean: clean_caches
clean_caches:
	find . -type d -name __pycache__    -print0 | xargs -0  rm -r
	find . -type d -name .pytest_cache  -print0 | xargs -0  rm -r
	rm -f ./.coverage
	rm -f ./.mutmut-cache

cleaner: clean
	rm -rf ${COVERAGE_dir}
	rm -rf ${MUTMUT_dir}
	rm -rf {PYREVERSE_DIR}*

cleanest veryclean: cleaner
