# (C) Albert Mietus, 2025. Part of Castle/CCastle project
pyanalyse: pyreverse py_classtree

# Local setting (see Mk/settings.mk for global settings
PYREVERSE_FORMAT  = svg
OPT_OUT           = -d ${PYANALYSE_dir} -o ${PYREVERSE_FORMAT}
OPT_COLOR         = --colorized    --max-color-depth 99
PYREVERSE_OPTIONS =  -A  --filter-mode ALL       ${OPT_COLOR}
PYREVERSE_COMPACT =  -A  --filter-mode PUB_ONLY  ${OPT_COLOR}


${PYANALYSE_dir}:; mkdir $@

pyreverse: ${PYANALYSE_dir}
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
		cd  ${PYANALYSE_dir}; plantuml -tsvg ./*.plantuml); fi
	@echo ".. done. Result; see: ./${PYANALYSE_dir}"


py_classtree classtree: ${PYANALYSE_dir} ${CLASSTREE_tool}
	for P in ${PYREVERSE_PKGS}; do \
		D=`echo $$P | sed 's@\.@/@g'`;\
		python ${CLASSTREE_tool}  --html -Mm $${D}  >${PYANALYSE_dir}classtree-$${P}.html ;\
	done



