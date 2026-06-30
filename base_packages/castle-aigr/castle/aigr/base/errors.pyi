# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.base.errors``.
# Hand-maintained "manual autodoc" companion to errors.py.

class AIGR_ERROR(Warning):
    """Base class for every AIGR error.

    It derives from ``Warning`` (not ``Exception``) so AIGR problems are, by
    default, recoverable signals. The errors are intentionally *not* AIGR
    nodes -- they are not part of the represented tree.
    """

class NameError(AIGR_ERROR, AttributeError):
    """Raised when a looked-up name (``ID``) does not exist in a namespace."""

class PartError(AIGR_ERROR, AttributeError, LookupError):
    """Raised for an illegal ``Part`` access (attribute/index) -- see ``expressions.Part``."""
