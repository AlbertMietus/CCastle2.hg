# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.translators.base``.

import typing as PTH
from abc import abstractmethod, ABC, ABCMeta
from pathlib import Path

PYPY2_BINd: str
"""Hard-coded path to the PyPy2 binary directory (platform-specific)."""
TIMEOUT: int
"""Default subprocess timeout in seconds (60)."""


class TranslatorCommand(ABC):
    """Abstract base for commands that drive an external translator process.

    Subclasses implement :meth:`runner` to invoke the actual command (e.g.
    ``python``, ``rpython``).  The template :meth:`execute` calls
    :meth:`setup`, :meth:`runner`, :meth:`teardown` in order.

    Usage
    -----
    Subclass and override :meth:`runner`::

        class MyTranslator(TranslatorCommand):
            def runner(self):
                return self.process(["mytool", "input.py"])

        MyTranslator().execute()
    """

    @abstractmethod
    def runner(self) -> PTH.Union[str, PTH.Any]:
        """Run the external command and return its output.  Override in subclasses."""
        ...

    def execute(self) -> PTH.Union[str, PTH.Any]:
        """Run setup -> runner -> teardown and return the result."""
        ...

    def setup(self) -> None:
        """Called before :meth:`runner`; no-op by default."""
        ...

    def teardown(self) -> None:
        """Called after :meth:`runner`; no-op by default."""
        ...


class RPY_Translator(TranslatorCommand, metaclass=ABCMeta):
    """Concrete base for translators that drive the RPython toolchain.

    Manages a working directory, a list of files, a driver file, an output
    name, and a timeout.  Concrete subclasses (:class:`Evaluate`,
    :class:`Compile`, :class:`Execute`) implement :meth:`runner` to invoke
    the appropriate tool.

    Warning: ``RPYTHON`` and ``PYPY2_BINd`` are hard-coded paths.

    Usage
    -----
    ::

        from castle.writers.RPy.translators import Evaluate

        result = Evaluate(inDir="build/", driver="main").execute()
        # -> stdout of ``python main.py``
    """

    RPYTHON: PTH.ClassVar[str]
    """Path to the ``rpython`` binary (platform-specific, hard-coded)."""

    files: list[Path]
    """List of source files (converted to :class:`Path` on construction)."""
    driver: PTH.Optional[str]
    """File stem of the entry-point driver script."""
    inDir: Path
    """Working directory for the subprocess."""
    into: PTH.Optional[str]
    """Name of the produced output binary (if any)."""

    def __init__(
        self,
        *,
        inDir: PTH.Optional[PTH.Union[Path, str]] = ...,
        files: PTH.Union[list[PTH.Union[Path, str]], str] = ...,
        driver: PTH.Optional[str] = ...,
        into: PTH.Optional[str] = ...,
        timeout: int = ...,
    ) -> None: ...

    def process(
        self,
        cmd: list[str],
        *,
        PATH_prefix: PTH.Optional[str] = ...,
    ) -> str:
        """Run *cmd* as a subprocess in :attr:`inDir` and return stdout.

        Raises ``AssertionError`` on non-zero exit or timeout.
        """
        ...
