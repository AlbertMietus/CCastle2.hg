default all: run exe
demo: run exe

TARGET=main_HW

## 'run' with cpython
## 'exe' with rpython translor
RUNd= _run/
EXEd= _exe/

${RUNd} ${EXEd}:; mkdir $@

## Which translor: select dir with `PyPy_Vd`
PYPY_HGd	= /Users/albert/NoTimeMachine/PyPy,hgs/
#PyPy_Vd	= PyPy.release-pypy2.7-v7.x/
PyPy_Vd		= PyPy.dev/
PYPY_SRCd	= ${PYPY_HGd}${PyPy_Vd}
RPYTHON		= ${PYPY_SRCd}./rpython/bin/rpython
PYPY_APPSd	= /Users/albert/Apps/PyPy/
PYPY2_BINd	= ${PYPY_APPSd}./pypy2.7-v7.3.12-macos_arm64/bin/
TRANSLOR	= PATH=${PYPY2_BINd}:$$PATH ${RPYTHON} --no-pdb

RPY_files := $(wildcard *.rpy)
PY_files_RUN := $(patsubst %.rpy,${RUNd}%.py,${RPY_files})
PY_files_EXE := $(patsubst %.rpy,${EXEd}%.py,${RPY_files})


${PY_files_RUN}: ${RUNd}%.py  : %.rpy
	cp $< $@
${PY_files_EXE}: ${EXEd}%.py  : %.rpy
	cp $< $@

run: run_${TARGET}
run_${TARGET}: ${RUNd} ${PY_files_RUN}
	@echo "========== $@ =========="
	@cd ${RUNd}; python ${TARGET}.py
	@echo "========== $@ =========="

exe: exe_${TARGET}
exe_${TARGET}: ${EXEd} ${EXEd}${TARGET}
	@echo "========== $@ =========="
	@./${EXEd}${TARGET}
	@echo "========== $@ =========="

${EXEd}${TARGET}: ${PY_files_EXE}
	cd ${EXEd} ;\
	${TRANSLOR} --output=${TARGET} main_HW.py



clean: clean_run clean_exe
cleaner: clean

clean_run:
	rm -rf ${RUNd}

clean_exe: # Do not remove the dirs, as the are include dirs
	rm -f ${PY_files_EXE}
	rm -f ./${EXEd}${TARGET}
	rm -f ./${EXEd}*.py ./${EXEd}*.pyc


veryclean very_clean cleanest: cleaner

#Manual dependendies
_run/HelloWorld.py : HelloWorld.rpy
_translated/HelloWorld.py : HelloWorld.rpy
