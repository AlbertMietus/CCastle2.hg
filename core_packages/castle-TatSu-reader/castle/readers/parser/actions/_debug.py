# (C) Albert Mietus, 2025. Part of Castle/CCastle project
_log_name = '.'.join(__name__.split(".")[:-1])
import logging; logger = logging.getLogger(_log_name)

from functools import wraps


def add_debug_logging(cls):
    """Class decorator to add debug logging to all methods."""
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):  # Only wrap methods
            setattr(cls, attr_name, _wrap_with_logging(cls.__name__, attr_name, attr_value))
    return cls


def _wrap_with_logging(class_name, method_name, method):
    """Wrap a method to add debug logging using a file-level logger."""
    @wraps(method)
    def wrapper(self, ast, *args, **kwargs):
        retval = method(self, ast, *args, **kwargs)
        logger.debug(f"{class_name}.{method_name}::\t{ast=} ==> retval={retval} ---- {args=}, {kwargs=}")
        return retval
    return wrapper

