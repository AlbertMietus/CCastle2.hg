CC2CpyNote:
	@echo "$@:\n==========="
	@echo "The CC2Cpy backend (writer) is abandoned (for now). 	\
	The focus is shifted towards rPY."
	@echo "There are a few reasons:\n\
	  - CC2Cpy is using manually rendering routines;\n\
            It was simple to start, but (too) complex to maintain\n\
	  - CC2Cpy, with it C-background has limitations with (e.g.) namespaces,\n\
	    See: http://docideas.mietus.nl/en/default/CCastle/3.Design/B.Workshop/CC2Cpy/zz.todo.html\n\
	  - RPython is fun (http://docideas.mietus.nl/en/default/CCastle/3.Design/B.Workshop/rPY/index.html)\n"

CC2Cpy_LAST = \
	pyt0st/writers/CC2Cpy/test_2a_groundwork.py		\
	pytst/writers/CC2Cpy/test_2b_EventProtocol.py		\
	pytst/writers/CC2Cpy/test_3a_CompPorts.py 		\
	pytst/writers/CC2Cpy/test_3b_CompInterface.py		\
	pytst/writers/CC2Cpy/test_3c_CompImpl.py		\
#
CC2Cpy_CURRENT = \
	pytst/writers/CC2Cpy/test_4a_HandlerTables.py 		\
	pytst/writers/CC2Cpy/test_9_genSieve.py			\
#
CC2Cpy_TODO = \
	pytst/writers/CC2Cpy/test_999_NoNameCollision.py	\
#
CC2Cpy: CC2CpyNote


CC2Cpy_last:;		make last    LAST="${CC2Cpy_LAST}"
CC2Cpy_current:;	make current CURRENT="${CC2Cpy_CURRENT}"
CC2Cpy_todo:;		make toto    TODO="${CC2Cpy_TODO}"
