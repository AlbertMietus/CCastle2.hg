default: all
all: hand_crafted
try:  HC_cpython HC_pypy2
translate: translate_HC



PYPY2_BINd	= /Users/albert/Apps/PyPy/pypy2.7-v7.3.20-macos_arm64/bin/
RPYTHON_exe = ${PYPY2_BINd}./rpython

## Albert's version of rpython (driver) contains the path
TRANSLOR	= ${RPYTHON_exe} --batch

HCd=handCrafted/
HC_rpy=HelloWorld_rpy.py
HC_exe=HelloWorld.exe

hand_crafted: HC
HC:  HC_cpython HC_pypy2 run_HC

HC_cpython: ${HCd}${HC_rpy}
	@echo "========== $@ ==========($<)"
	python $<
	@echo "========= /$@ =========="
	@echo

HC_pypy2: ${HCd}${HC_rpy}
	@echo "========== $@ ==========($<)"
	pypy2  $<
	@echo "========= /$@ =========="
	@echo

run_HC: translate_HC
	@echo "========== $@ ==========($<)"
	cd ${HCd} ;./${HC_exe}
	@echo "========= /$@ =========="
	@echo

translate_HC: ${HCd}/${HC_exe}
${HCd}/${HC_exe} : ${HCd}${HC_rpy}
	@echo "========== $@ ==========($<)"
	cd ${HCd}		;\
	${TRANSLOR} --output=${HC_exe} ${HC_rpy}
	@echo "========= /$@ =========="
	@echo



clean: clean_HC

clean_HC:
	rm -f ${HCd}${HC_exe}
	rm -f ${HCd}*.pyc
	rm -rf  ${HCd}__pycache__
