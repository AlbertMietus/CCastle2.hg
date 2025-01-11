default: sub-build


SUBS =\
	base_packages/			\
	TestDoubles_packages/	\
	core_packages/			\
#


include ${TOPd}Mk/dirs.mk

.PHONY: TAGS etags tags
TAGS etags tags:
	find . -name "*.py" -print | etags -


