# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions._debug``.
# Hand-maintained companion to _debug.py.

import typing as PTH

_log_name: str
logger: PTH.Any

_ClsT = PTH.TypeVar("_ClsT", bound=type)


def add_debug_logging(cls: _ClsT) -> _ClsT:
    """Class decorator that wraps every callable method with DEBUG-level logging.

    After decoration each method logs a line of the form::

        ClassName.method_name::  ast=<value> ==> retval=<result>

    to the parent-package logger at ``logging.DEBUG`` level before returning
    the original result.  Applied to every semantic-action class in this package
    so that ``castle.readers.ladon.parser.actions`` DEBUG messages can be toggled
    with a single logger level change.

    The decorated class is returned unchanged as far as the public API is
    concerned; the decorator replaces each method with a ``functools.wraps``-
    wrapped version, so ``__name__`` and docstrings are preserved.
    """
    ...


def _wrap_with_logging(
    class_name: str,
    method_name: str,
    method: PTH.Callable[..., PTH.Any],
) -> PTH.Callable[..., PTH.Any]:
    """Return a ``functools.wraps``-wrapped version of *method* that logs its call."""
    ...
