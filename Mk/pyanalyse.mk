PYREVERSE_DIR=_pyreversed/
PYREVERSE_FORMAT=svg
PYREVERSE_OPTIONS=-k -A
PYREVERSE_OPTIONS=-A
PYREVERSE_PRJS= castle castle.readers castle.ast  castle.aigr TestDoubles.AIGR

pyanalyse pyreverse: ${PYREVERSE_DIR}
	for P in ${PYREVERSE_PRJS}; do \
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYREVERSE_DIR} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-noModules -mn --colorized --max-color-depth=42  $$P >>/dev/null;\
		pyreverse -d ${PYREVERSE_DIR} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-Modules -my --colorized --max-color-depth=42  $$P >>/dev/null;\
	done
	@echo ".. done. Result; see: ./${PYREVERSE_DIR}"
#	@ls -l ${PYREVERSE_DIR}/*.${PYREVERSE_FORMAT}

