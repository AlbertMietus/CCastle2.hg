
# Local setting (see Mk/settings.mk for global settings
PYREVERSE_OPTIONS =  -k -A
PYREVERSE_OPTIONS =  -A

# Default project/compinets name (dirs & subdirs) --overrule in Local Makefile
PYREVERSE_PRJS	  ?=  castle

pyanalyse pyreverse: ${PYREVERSEd}
	for P in ${PYREVERSE_PRJS}; do \
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYREVERSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-noModules -mn --colorized --max-color-depth=42  $$P >>/dev/null;\
		pyreverse -d ${PYREVERSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-Modules   -my --colorized --max-color-depth=42  $$P >>/dev/null;\
	done
	@echo ".. done. Result; see: ./${PYREVERSE_dir}"


