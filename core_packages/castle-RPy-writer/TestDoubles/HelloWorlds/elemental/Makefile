default: none

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


run: run_HW
run_HW: ${RUNd} ${PY_files} ${CCln}
	cd ${RUNd}; python HelloWorld.py


clean:;
	@echo Noting to do
	@echo "	Use  make cleaner -- to remove ${RUNd}"

cleaner: 
	rm -rf ${RUNd}

