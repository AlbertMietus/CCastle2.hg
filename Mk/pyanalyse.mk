
# Local setting (see Mk/settings.mk for global settings
PYREVERSE_OPTIONS =  -k -A
PYREVERSE_OPTIONS =  -A


${PYREVERSE_dir}:; mkdir $@

pyanalyse pyreverse: ${PYREVERSE_dir}
	for P in ${PYREVERSE_PKGS}; do \
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYREVERSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-noModules -mn --colorized --max-color-depth=42  $$P ;\
		pyreverse -d ${PYREVERSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-Modules   -my --colorized --max-color-depth=42  $$P ;\
	done
	@echo ".. done. Result; see: ./${PYREVERSE_dir}"


