# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.loaders.simple_loader``.
# Hand-maintained companion to simple_loader.py.

import typing as PTH
from pathlib import Path

from ._base_loader import _FileLoader

logger: PTH.Any


class SimpleFileLoader(_FileLoader):
    """Load and parse a Castle source file given a filesystem :class:`~pathlib.Path`.

    This is the **primary public entry point** for file-based Castle parsing.
    The TatSu start symbol is inferred from the file suffix (``.Castle`` or
    ``.Moat``) unless overridden via the *kind* keyword argument inherited from
    :class:`~._base_loader._BaseLoader`.

    Usage::

        from castle.readers.ladon.loaders import SimpleFileLoader
        from pathlib import Path

        loader     = SimpleFileLoader(Path("hello.Castle"))
        source_ns  = loader.parse()     # -> castle.aigr.Source_NS

    The returned :class:`~castle.aigr.Source_NS` can then be walked by a
    ``Visitor`` or passed to a writer (e.g. the RPy writer).
    """

    def __init__(self, file: PTH.Optional[Path], **kw: PTH.Any) -> None: ...


class PyModuleLoader(_FileLoader):
    """Load a Castle source file that is distributed inside an installed Python package.

    Resolves *file* relative to the package directory of the already-installed
    Python package *module*.  Useful for Castle files shipped as package data.

    Usage::

        from castle.readers.ladon.loaders.simple_loader import PyModuleLoader

        loader    = PyModuleLoader("my_castle_pkg", "MyComponent.Castle")
        source_ns = loader.parse()      # -> castle.aigr.Source_NS

    *module* must be importable (i.e. on ``sys.path``); an ``ImportError`` is
    raised immediately in ``__init__`` if it is not found.
    """

    def __init__(self, module: str, file: str, **kw: PTH.Any) -> None: ...
