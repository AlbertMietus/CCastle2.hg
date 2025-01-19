default: none

TARGET=main_HW

RUNd= _run/

CCln 	=	${RUNd}CC
CCorg	= ../../../../castle/writers/RPy/CC # rel _run

RPY_files := $(wildcard *.rpy)
PY_files := $(patsubst %.rpy,${RUNd}%.py,${RPY_files})

${RUNd}:
	mkdir $@

${PY_files}: ${RUNd}%.py  : %.rpy
	cp $< $@


${CCln}: ${RUNd}
	@if [ ! -x ${CCln} ] ; then 	\
	  echo ln -s ${CCorg} ${CCln} 	;\
	  ln -s ${CCorg} ${CCln} 		;\
	fi


run: run_${TARGET}
run_${TARGET}: ${RUNd} ${PY_files} ${CCln}
	@echo ; echo "run ${TARGET}"
	cd ${RUNd}; python ${TARGET}.py

rpy2py:${PY_files}
clean:;
	@echo Noting to do
	@echo "	Use  make cleaner -- to remove ${RUNd}"

cleaner: 
	rm -rf ${RUNd}

veryclean very_clean cleanest: cleaner
