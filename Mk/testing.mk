PYTEST= pytest
PYTEST_OPTONS=-rxXsfE

test: coverage local_test
local_test:: # Add local module test to this one

coverage:
	coverage run  --source castle,pytst --branch -m pytest ${PYTEST_OPTONS} pytst/
	coverage report  --skip-covered
	coverage html --directory=${COVERAGE_dir}
coverage-open: coverage
	open ${COVERAGE_dir}index.html

pytest pytest-only:							# No coverage reports
	${PYTEST} ${PYTEST_OPTONS}  pytst
pytest-s:								# -s : No capure (so, show stdout/stderr)
	${PYTEST} ${PYTEST_OPTONS} -s pytst
pytest-d pytest-ds pytest-sd:						# with debuging
	${PYTEST} ${PYTEST_OPTONS} --log-cli-level=DEBUG -s pytst/

# Mutation testing (takes a long run) https://en.wikipedia.org/wiki/Mutation_testing -- not part of 'all'
mutmut: ${ToCS_dir}
	-PYTHONPATH=${MUTMUT_cfg_d}	mutmut run  --tests-dir pytst --paths-to-mutate castle  --runner "pytest -x   pytst/"
	mutmut html && rm -rf ${MUTMUT_dir} && mv html ${MUTMUT_dir}
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

