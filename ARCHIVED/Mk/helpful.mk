demo: pytest-demo python-demo

python-demo:
	@echo Running all 'dem*.py' python-files
	export PYTHONPATH=`pwd`; for d in `find demos -type f -iname \*.py `; do echo "=== $$d ==="; python $$d; echo "=========="; done

pytest-demo:
	-PYTHONPATH=`pwd` pytest -s demos || echo "currently NO pytest-demos (check/fix manually)"

