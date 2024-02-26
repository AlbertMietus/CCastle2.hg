clean: clean_caches
cleaner: clean clean_gendirs
cleanest veryclean: cleaner clean_generated

clean_caches:
	find . -type d -name __pycache__    -print0 | xargs -0  rm -r
	find . -type d -name .pytest_cache  -print0 | xargs -0  rm -r
	rm -rf ./.coverage
	rm -rf ./.mutmut-cache
	rm -rf ./.mypy_cache

clean_gendirs:
	rm -rf ${COVERAGE_dir}
	rm -rf ${MUTMUT_dir}
	rm -rf ${PYREVERSE_dir}*

clean_generated:
	# None, for now
