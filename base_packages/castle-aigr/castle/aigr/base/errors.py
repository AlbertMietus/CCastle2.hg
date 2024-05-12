# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

#Note: Errors do not inherit for AIGR, as they are not part of the "tree"

class AIGR_ERROR(Warning):
    "Base class for all errors in AIGR"

class NameError(AIGR_ERROR, AttributeError):
    "This name (or ID) does not exits, when looking for it"


class PartError(AIGR_ERROR, AttributeError,LookupError):
    "An error for Part (generalisation of Index & Attribute operations)"

