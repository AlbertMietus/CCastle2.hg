# Makefile -- GNU syntax 			(C) 2000-2016 reuse freely -- http://ALbert.mietus.nl

###
### recursive::  Generic macro to run sub-makes, in each dir in SUBS
###

include ${TOPd}Mk/settings.mk
TARGETS = $(sort ${FULL})

RECURSIVE_TARGETS =  $(foreach dir,$(SUBS),$(foreach target,$(TARGETS),$(dir)/$(target)))

.PHONY: ${TARGETS}  ${SUBS} ${RECURSIVE_TARGETS}

$(TARGETS): % : $(foreach dir,$(SUBS),$(dir)/%)
$(SUBS)  : % : %/all

${RECURSIVE_TARGETS}:
	$(MAKE) -C $(dir $@)  $(notdir $@)

# re-test: clean first, then test
retest : clean test

recursive_show:
	@echo FULL: 	${FULL}
	@echo TARGETS: 	${TARGETS}
	@echo SUBS: 	${SUBS}
	@echo RECURSIVE_TARGETS: ${RECURSIVE_TARGETS}
