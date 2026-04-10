# (C) Albert Mietus, 2025. Part of Castle/CCastle project
pyanalyse: pyreverse py_classtree

# Local setting (see Mk/settings.mk for global settings
PYREVERSE_OPTIONS =  -k -A
PYREVERSE_OPTIONS =  -A
PYREVERSE_OPTIONS =  -A --filter-mode ALL  --colorized    --max-color-depth 99
PYREVERSE_FORMAT  = svg

${PYANALYSE_dir}:; mkdir $@

pyreverse: ${PYANALYSE_dir}
	for P in ${PYREVERSE_PKGS}; do \
		P=`echo $$P | sed 's@\.@/@g'`;\
		echo "PYANALYSE::" $$P "...";\
		pyreverse -d ${PYANALYSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-noModules -mn --max-color-depth=42  $$P & \
		pyreverse -d ${PYANALYSE_dir} -o ${PYREVERSE_FORMAT} ${PYREVERSE_OPTIONS} -p $$P-Modules   -my --max-color-depth=42  $$P & \
	done
	wait
	if [ "plantuml" = ${PYREVERSE_FORMAT} ] ;then (\
		echo "PYANALYSE: plantUML processing (all)"; \
		cd  ${PYANALYSE_dir}; plantuml -tsvg ./*.plantuml); fi
	@echo ".. done. Result; see: ./${PYANALYSE_dir}"


CLASSTREE_tool = ${TOPd}../tools/classtree

py_classtree classtree: ${PYANALYSE_dir}
	for P in ${PYREVERSE_PKGS}; do \
		D=`echo $$P | sed 's@\.@/@g'`;\
		${CLASSTREE_tool}  --html -Mm $${D}  >${PYANALYSE_dir}classtree-$${P}.html ;\
	done



