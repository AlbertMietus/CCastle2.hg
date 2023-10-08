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


PYREVERSE_DIR=_pyreversed/
PYREVERSE_FORMAT=svg
PYREVERSE_OPTIONS=-k -A
PYREVERSE_OPTIONS=-A
PYREVERSE_PRJS= castle castle.readers castle.ast castle.writers.CC2Cpy castle.aigr TestDoubles.AIGR

pyanalyse pyreverse: ${PYREVERSE_DIR}
	for P in ${PYREVERSE_PRJS}; do \
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYREVERSE_DIR} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-noModules -mn --colorized --max-color-depth=42  $$P >>/dev/null;\
		pyreverse -d ${PYREVERSE_DIR} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-Modules -my --colorized --max-color-depth=42  $$P >>/dev/null;\
	done
	@echo ".. done. Result:"
	@ls -l ${PYREVERSE_DIR}/*.${PYREVERSE_FORMAT}

