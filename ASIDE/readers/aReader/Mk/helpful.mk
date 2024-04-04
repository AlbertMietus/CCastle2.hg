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


