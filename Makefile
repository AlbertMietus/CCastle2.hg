default: sub-build


SUBS =\
	base_packages/castle-aigr			\
	base_packages/castle-monorail			\
	TestDoubles_packages/TestDoubles-aigr-sieve	\
	core_packages/castle-RPy-writer			\
#


include ${TOPd}Mk/dirs.mk

.PHONY: TAGS etags tags
TAGS etags tags:
	find . -name "*.py" -print | etags -


