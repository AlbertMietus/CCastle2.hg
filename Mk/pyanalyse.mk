
# Local setting (see Mk/settings.mk for global settings
PYREVERSE_OPTIONS =  -k -A
PYREVERSE_OPTIONS =  -A


${PYREVERSE_dir}:; mkdir $@

pyanalyse pyreverse: ${PYREVERSE_dir}
	for P in ${PYREVERSE_PKGS}; do \
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYREVERSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-noModules -mn --max-color-depth=42  $$P & \
		pyreverse -d ${PYREVERSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-Modules   -my --max-color-depth=42  $$P & \
	done
	wait
	if [ "plantuml" = ${PYREVERSE_FORMAT} ] ;then (\
		echo "PYANALYSE: plantUML processing (all)"; \
		cd  ${PYREVERSE_dir}; plantuml -tsvg ./*.plantuml); fi
	@echo ".. done. Result; see: ./${PYREVERSE_dir}"



pyanalyse-open: pyanalyse
	open ./${PYREVERSE_dir}/*.${PYREVERSE_FORMAT}

