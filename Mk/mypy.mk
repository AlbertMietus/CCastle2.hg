mypy: mypy_castle

#DOC: mypy will complain with 'Module "castle.aigr" has no attribute "types"  [attr-defined]' (and such)
## triggered by lines `from castle.aigr import types` as aigr import .base  and base .types ... - which is fine (IMHO)
### Changing the import to `from castle.aigr.base import types` (make .base. explicit) silences the error.
### Note: in both case, the pytest works fine ...
## I don't like the add .base. .... IMHO in unhides details
### So, we can ignore that error with ``--follow-imports=skip``
### Note: there is some discussion online on this, maybe it a "bug" in v1.13.0 .. we will see


mypy_castle:
	@echo "MYPY::"
	mypy	--follow-imports=skip --exclude=/_ref/ 	castle
	mypy	--follow-imports=skip --exclude=/_ref/ 	pytst


