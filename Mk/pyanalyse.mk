# (C) Albert Mietus, 2025. Part of Castle/CCastle project


# Local setting (see Mk/settings.mk for global settings
PYREVERSE_FORMAT  = svg

OPT_OUT           = -d ${PYREVERSE_dir} -o ${PYREVERSE_FORMAT} 
OPT_COLOR         = --colorized    --max-color-depth 99

PYREVERSE_OPTIONS =  -A  --filter-mode ALL       ${OPT_COLOR}
PYREVERSE_COMPACT =  -A  --filter-mode PUB_ONLY  ${OPT_COLOR}

${PYREVERSE_dir}:; mkdir $@

pyanalyse pyreverse: ${PYREVERSE_dir}
	for P in ${PYREVERSE_PKGS}; do \
		P=`echo $$P | sed 's@\.@/@g'`;\
		echo "PYANALYSE::" $$P "...";\
		pyreverse  ${OPT_OUT} ${PYREVERSE_OPTIONS}    -p $$P-noModules -mn    $$P & \
		pyreverse  ${OPT_OUT} ${PYREVERSE_OPTIONS}    -p $$P-Modules   -my    $$P & \
		pyreverse  ${OPT_OUT} ${PYREVERSE_COMPACT}    -p $$P-compact-y   -my    $$P & \
	done
	wait
	if [ "plantuml" = ${PYREVERSE_FORMAT} ] ;then (\
		echo "PYANALYSE: plantUML processing (all)"; \
		cd  ${PYREVERSE_dir}; plantuml -tsvg ./*.plantuml); fi
	@echo ".. done. Result; see: ./${PYREVERSE_dir}"


pyanalyse-open: pyanalyse
	open ./${PYREVERSE_dir}/*.${PYREVERSE_FORMAT}

