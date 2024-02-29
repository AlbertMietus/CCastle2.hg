PYTEST=PYTHONPATH=`pwd` pytest
PYTEST_OPTONS=-rxXsfE

test coverage:
	coverage run --branch -m pytest ${PYTEST_OPTONS}  pytst/
	coverage report  --skip-covered
	coverage html --directory=${COVERAGE_dir}
coverage-open: coverage
	open ${COVERAGE_dir}index.html

pytest pytest-only:							# No coverage reports
	pytest ${PYTEST_OPTONS}  pytst
pytest-s:								# -s : No capure (so, show stdout/stderr)
	pytest ${PYTEST_OPTONS} -s pytst
pytest-d pytest-ds pytest-sd:						# with debuging
	pytest ${PYTEST_OPTONS} --log-cli-level=DEBUG -s pytst/

mutmut: # Mutation testing (takes a long run) https://en.wikipedia.org/wiki/Mutation_testing
	-mutmut run  --paths-to-exclude ARCHIVED --tests-dir pytst --paths-to-mutate castle  --runner "pytest -x   pytst/"
	mutmut html && rm -rf ${MUTMUT_dir} && mv html ${MUTMUT_dir}
	mutmut results
mutmut-open: mutmut
	open ${MUTMUT_dir}index.html



last:
	${PYTEST}  ${PYTEST_OPTONS}  ${LAST}
current:
	${PYTEST}  ${PYTEST_OPTONS}  ${CURRENT}
current-ds current-sd:
	${PYTEST}  ${PYTEST_OPTONS}  --log-cli-level=DEBUG -s ${CURRENT}
current-info:
	${PYTEST}  ${PYTEST_OPTONS}  --log-cli-level=INFO -s ${CURRENT}
recheck:
	${PYTEST}  ${PYTEST_OPTONS}   ${LAST} ${CURRENT}
todo:
	${PYTEST}  ${PYTEST_OPTONS}  ${TODO}

