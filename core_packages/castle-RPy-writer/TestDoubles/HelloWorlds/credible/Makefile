default: hand_crafted

## Which translor: select dir with `PyPy_Vd`
PYPY_HGd	= /Users/albert/NoTimeMachine/PyPy,hgs/
#PyPy_Vd	= PyPy.release-pypy2.7-v7.x/
PyPy_Vd		= PyPy.dev/
PYPY_SRCd	= ${PYPY_HGd}${PyPy_Vd}
RPYTHON		= ${PYPY_SRCd}./rpython/bin/rpython
PYPY_APPSd	= /Users/albert/Apps/PyPy/
PYPY2_BINd	= ${PYPY_APPSd}./pypy2.7-v7.3.12-macos_arm64/bin/
TRANSLOR	= PATH=${PYPY2_BINd}:$$PATH ${RPYTHON} --no-pdb

HCd=handCrafted/
HC_rpy=HelloWorld_rpy.py
HC_exe=HelloWorld.exe

hand_crafted: HC
HC:  HC_cpython HC_pypy2 run_HC

HC_cpython: ${HCd}${HC_rpy}
	python $<
HC_pypy2: ${HCd}${HC_rpy}
	pypy2  $<
run_HC: translate_HC
	-echo run rpython-translated $<
	cd ${HCd} ;./${HC_exe}
translate_HC: ${HCd}/${HC_exe}
${HCd}/${HC_exe} : ${HCd}${HC_rpy}
	-echo rpython-translate $<
	cd ${HCd}		;\
	${TRANSLOR} --output=${HC_exe} ${HC_rpy}



