# (C) Albert Mietus, 2025. Part of Castle/CCastle project

PYTEST= pytest
PYTEST_OPTIONS=-rxXsfE
PYTEST_OPTIONS_NOxFAIL=-rXsfE

PYFAST= ${PYTEST} ${PYFAST_OPTON}

PACKAGE:= $(shell basename `pwd`)

test: coverage local_test
local_test:: # Add local module test to this one

coverage:
	coverage run  --source castle,pytst --branch -m pytest ${PYTEST_OPTIONS} pytst/
	coverage report  --skip-covered
	coverage html --directory=${COVERAGE_dir} --title="CCaste:: '${PACKAGE}' coverage report"
coverage-open: coverage
	open ${COVERAGE_dir}index.html

list-tests list-test list_tests list_test collect-only: pytest-collect

pytest-show pytest-collect:
	${PYTEST} --collect-only ${PYTEST_OPTIONS}  pytst
pytest pytest-only:							# No coverage reports
	${PYTEST} ${PYTEST_OPTIONS}  pytst
pytest-s:								# -s : No capure (so, show stdout/stderr)
	${PYTEST} ${PYTEST_OPTIONS} -s pytst
pytest-d pytest-ds pytest-sd:						# with debuging
	${PYTEST} ${PYTEST_OPTIONS} --log-cli-level=DEBUG -s pytst/
pytest-info:						# with debuging at INFO level
	${PYTEST} ${PYTEST_OPTIONS} --log-cli-level=info  -s pytst/

# Mutation testing (takes a long run) https://en.wikipedia.org/wiki/Mutation_testing -- not part of 'all'
mutmut: mutmut3
mutmut3:
	echo "Mutmut3 not working yet"
	mutmut run
	mutmut results


last:
	${PYFAST}  ${PYTEST_OPTIONS_NOxFAIL}  ${LAST}
last-info:
	${PYFAST}  ${PYTEST_OPTIONS_NOxFAIL}  --log-cli-level=INFO -s ${LAST}
current:
	${PYFAST}  ${PYTEST_OPTIONS}  -s ${CURRENT}
current-ds current-sd:
	${PYFAST}  ${PYTEST_OPTIONS}  --log-cli-level=DEBUG -s ${CURRENT}
current-info:
	${PYFAST}  ${PYTEST_OPTIONS}  --log-cli-level=INFO -s ${CURRENT}
todo:
	${PYFAST}  ${PYTEST_OPTIONS}  ${TODO}
recheck:
	${PYFAST}  ${PYTEST_OPTIONS}   ${LAST} ${CURRENT}
fast:
	${PYFAST}  ${PYTEST_OPTIONS}  pytst
