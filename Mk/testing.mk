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

last:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${LAST}
current-only:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${CURRENT}
current:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${CURRENT} ${TODO}
todo:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  ${TODO}
current-ds current-sd:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  --log-cli-level=DEBUG -s ${CURRENT}
current-info:
	PYTHONPATH=`pwd` pytest ${PYTEST_OPTONS}  --log-cli-level=INFO -s ${CURRENT}

clean: clean_caches
