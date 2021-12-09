# Makefile -- GNU syntax 			(C) 2000-2016 reuse freely -- http://ALbert.mietus.nl

###
### recursive::  Generic macro to run sub-makes, in each dir in SUBS
###

# all possible recursive targets ..
RECURSIVE	  =  clean all test docs cleaner cleanest demos
RECURSIVE_TARGETS =  $(foreach dir,$(SUBS),$(foreach target,$(RECURSIVE),$(dir)/$(target)))

.PHONY: ${RECURSIVE}  ${SUBS} ${RECURSIVE_TARGETS}

$(RECURSIVE): % : $(foreach dir,$(SUBS),$(dir)/%)
$(SUBS)  : % : %/all

${RECURSIVE_TARGETS}:
	$(MAKE) -C $(dir $@)  $(notdir $@)

# re-test: clean first, then test
retest : clean test
veryclean: cleanest

help-local::
	@echo RECURSIVE: ${RECURSIVE}
	@echo SUBS: ${SUBS}
	@echo RECURSIVE_TARGETS: ${RECURSIVE_TARGETS}
